// Guardrails function for Voiceflow. 
// ref: https://cookbook.openai.com/examples/how_to_use_guardrails

/**
 * Main function that performs the guardrail checks and returns the appropriate response.
 * @param {Object} args - The input arguments.
 * @returns {Object} - The response object.
 */
export default async function main(args) {
    // Extract input variables from args
    const { openaiApiKey, userRequest } = args.inputVars;

    // Validate that the required input variables are provided
    if (!userRequest || !openaiApiKey) {
        return {
            next: { path: 'error' },
            trace: [{ type: "debug", payload: { message: "Missing required input variable: userRequest or openaiApiKey" } }]
        };
    }

    // Define the URL for the OpenAI API
    const url = `https://api.openai.com/v1/chat/completions`;

    /**
     * Function to check the topical guardrail.
     * @returns {string} - The guardrail response.
     * @throws {Error} - If there is an HTTP error.
     */
    async function checkTopicalGuardrail() {
        const guardrailData = {
            model: "gpt-4o-mini",
            messages: [
                {
                    "role": "system",
                    "content": "Your role is to assess whether the user question is allowed or not. The allowed topics are cats and dogs. If the topic is allowed, say 'allowed' otherwise say 'not_allowed'",
                },
                {"role": "user", "content": userRequest},
            ],
            temperature: 0
        };

        const guardrailConfig = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${openaiApiKey}`
            },
            body: JSON.stringify(guardrailData)
        };

        const guardrailResponse = await fetch(url, guardrailConfig);
        if (!guardrailResponse.ok) {
            throw new Error(`HTTP error! status: ${guardrailResponse.status}`);
        }
        const guardrailBody = await guardrailResponse.json;
        return guardrailBody.choices[0].message.content;
    }

    /**
     * Function to get the chat response.
     * @returns {string} - The chat response.
     * @throws {Error} - If there is an HTTP error.
     */
    async function getChatResponse() {
        const chatData = {
            model: "gpt-4o-mini",
            messages: [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": userRequest},
            ],
            temperature: 0.5
        };

        const chatConfig = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${openaiApiKey}`
            },
            body: JSON.stringify(chatData)
        };

        const chatResponse = await fetch(url, chatConfig);
        if (!chatResponse.ok) {
            throw new Error(`HTTP error! status: ${chatResponse.status}`);
        }
        const chatBody = await chatResponse.json;
        return chatBody.choices[0].message.content;
    }

    try {
        const guardrailResponse = await checkTopicalGuardrail();
        if (guardrailResponse === "not_allowed") {
            return {
                outputVars: { completion: "I can only talk about cats and dogs, the best animals that ever lived." },
                next: { path: 'success' },
                trace: [{ type: "text", payload: { message: "Topical guardrail triggered" } }]
            };
        } else {
            const chatResponse = await getChatResponse();
            return {
                outputVars: { completion: chatResponse },
                next: { path: 'success' },
                trace: [{ type: "text", payload: { message: chatResponse } }]
            };
        }
    } catch (error) {
        return {
            next: { path: 'error' },
            trace: [{ type: "debug", payload: { message: "Error: " + error.message } }]
        };
    }
}