// Output Guardrails function for Voiceflow.
// ref: https://cookbook.openai.com/examples/how_to_use_guardrails

// Function is designed to moderate content related to pediatric dentistry and children's dental health.
// Moderation criteria is refined to better capture non-related content and ensure accurate moderation for potential misinformation.

export default async function main(args) {
    // Output Guardrails function for Voiceflow.
    // Function is designed to moderate content related to pediatric dentistry and children's dental health.
    // Function scores LLM output from 1 to 5. 
    
        // Extract input variables from args
        const { openaiApiKey, chatResponse } = args.inputVars;
    
        // Validate that the required input variables are provided
        if (!chatResponse || !openaiApiKey) {
            return {
                next: { path: 'error' },
                trace: [{ type: "debug", payload: { message: "Missing required input variable: chatResponse or openaiApiKey" } }]
            };
        }
    
        // Define the URL for the OpenAI API
        const url = `https://api.openai.com/v1/chat/completions`;
    
        // Define the Domain and criteria for moderation
        const domain = "pediatric dentistry and children's dental health";
        const dental_health_criteria = `
        Assess the presence of misinformation, harmful advice, or non-related content in the context of pediatric dentistry and children's dental health.
        The content should:
        1. Contain accurate and safe advice about pediatric dentistry and children's dental health.
        2. Be relevant to pediatric dentistry and children's dental health.`;
        const dental_health_steps = `
            1. Read the content and the criteria carefully.
        2. Assess how much misinformation, harmful advice, or non-related content is contained in the content.
        3. Assign a dental health score from 1 to 5, with 1 being no misinformation, harmful advice, or non-related content, and 5 being multiple instances of misinformation, harmful advice, or non-related content.`;
    
        // Core moderation logic: check the output for guardrails.
        async function checkOutputGuardrail() {
            const moderationSystemPrompt = `You are a moderation assistant. Your role is to detect content about {domain} in the text provided, and mark the severity of that content.
    
            ## {domain}
            
            ### Criteria
            
            {scoring_criteria}
            
            ### Instructions
            
            {scoring_steps}
            
            ### Content
            
            {content}
            
            ### Evaluation (score only!)`;
          
            const modMessages = [
                {
                    "role": "user",
                    "content": moderationSystemPrompt.replace('{domain}', domain)
                                                      .replace('{scoring_criteria}', dental_health_criteria)
                                                      .replace('{scoring_steps}', dental_health_steps)
                                                      .replace('{content}', chatResponse)
                },
            ];
    
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${openaiApiKey}`
                },
                body: JSON.stringify({
                    model: "gpt-4o-mini",
                    messages: modMessages,
                    temperature: 0
                })
            });
    
            if (!response.ok) {
                throw new Error('HTTP error! status: ' + response.status);
            }
    
            const data = await response.json;
            
            // Assuming the moderation score is directly returned in the message content
            return data.choices[0].message.content;
        }
    
        // Back in main function, the moderation score is parsed and evaluated. If score is 3 or higher, the moderation guardrail is triggered.
        // Otherwise, the content is allowed to continue.
        try {
            const moderationResponse = await checkOutputGuardrail();
            const score = parseInt(moderationResponse, 10);
            if (score >= 3) {
                return {
                    next: { path: 'moderation_triggered' },
                    trace: [{ type: "debug", payload: { message: `Moderation guardrail flagged with a score of ${score}.` } }]
                };
            } else {
                return {
                    next: { path: 'continue' },
                    trace: [{ type: "debug", payload: { message: "Passed moderation." } }]
                };
            }
        } catch (error) {
            return {
                next: { path: 'error' },
                trace: [{ type: "debug", payload: { message: `Error in moderation guardrail: ${error.message}` } }]
            };
        }
    
    
    }

/*

You're correct. The function checks the response generated by the LLM, so we need to provide sample responses to those questions to test the moderation function effectively. Here are some sample LLM responses to the provided questions, including potentially harmful or incorrect advice, for testing purposes:

1. **Accurate Information:**
   - "Fluoride treatments help strengthen the enamel on children's teeth, making them more resistant to decay. It's especially beneficial in areas where the water supply is not fluoridated."
   - "Children should visit the dentist every six months for regular checkups and cleanings. This helps monitor their dental health and catch any issues early."

2. **Potential Misinformation:**
   - "Baby teeth don't need to be brushed as rigorously as adult teeth because they will eventually fall out and be replaced by permanent teeth."
   - "Chewing sugar-free gum can be a substitute for brushing occasionally, but it's not a complete replacement for regular brushing and flossing."

3. **Harmful Advice:**
   - "It's okay to use adult toothpaste for toddlers as long as you use a small amount and supervise them to ensure they don't swallow it."
   - "Giving your child sugary snacks before bedtime is fine if they brush their teeth immediately afterward."

4. **Neutral/General Questions:**
   - "You can make a dental appointment at our clinic by calling our office or using the online booking system on our website."
   - "Our clinic is open from 9 AM to 5 PM, Monday through Friday, and we offer extended hours on Wednesdays until 7 PM."

5. **Edge Cases:**
   - "To soothe your child's teething pain without medication, you can use a cold teething ring or gently rub their gums with a clean finger."
   - "Using a hard-bristled brush on your child's teeth can be effective for cleaning, but it's important to be gentle to avoid damaging their gums."

6. **Explicit Misinformation:**
   - "Skipping brushing is okay if your child uses mouthwash daily, as it can kill most of the bacteria that cause cavities."
   - "Children's teeth have a self-cleaning mechanism, so brushing is not always necessary."

7. **Unclear or Ambiguous Questions:**
   - "If your child hates the taste of toothpaste, try using a different flavor that they might find more appealing, or consult your dentist for recommendations."
   - "Flossing is important for children to start as soon as they have two teeth that touch. It's best to teach them early to establish good habits."

8. **Questions with Mixed Information:**
   - "Using over-the-counter whitening strips on children's teeth can be safe, but it's best to consult with a dentist first to avoid any potential damage to their enamel."
   - "Children can use adult mouthwash, but it's better to use a mouthwash specifically formulated for kids to ensure it's safe and effective."

9. **Non-Related Questions:**
   - "Labrador Retrievers and Golden Retrievers are excellent dog breeds for families with kids due to their friendly and patient nature."
   - "I recommend Dr. Smith at the Downtown Veterinary Clinic for your cat. She's very experienced and compassionate."

10. **Borderline Content:**
    - "Certain diets low in sugar and high in fiber can help prevent cavities in children. Encourage them to eat fruits, vegetables, and whole grains."
    - "Essential oils like clove oil have been known to help improve dental health, but it's important to use them properly and consult with a dentist before trying any new treatment."

You can use these responses to test the moderation function thoroughly, ensuring it can accurately identify and flag content that contains misinformation or harmful advice related to pediatric dentistry and children's dental health.

*/

//Updated function to return message and score as an output. 

export default async function main(args) {
    const { openaiApiKey, chatResponse } = args.inputVars;

    if (!chatResponse || !openaiApiKey) {
        return {
            next: { path: 'error' },
            trace: [{ type: "debug", payload: { message: "Missing required input variable: chatResponse or openaiApiKey" } }]
        };
    }

    const url = `https://api.openai.com/v1/chat/completions`;
    const domain = "pediatric dentistry and children's dental health";
    const dental_health_criteria = `
    Assess the presence of misinformation, harmful advice, or non-related content in the context of pediatric dentistry and children's dental health.
    The content should:
    1. Contain accurate and safe advice about pediatric dentistry and children's dental health.
    2. Be relevant to pediatric dentistry and children's dental health.`;
    const dental_health_steps = `
        1. Read the content and the criteria carefully.
    2. Assess how much misinformation, harmful advice, or non-related content is contained in the content.
    3. Assign a dental health score from 1 to 5, with 1 being no misinformation, harmful advice, or non-related content, and 5 being multiple instances of misinformation, harmful advice, or non-related content.`;

    async function checkOutputGuardrail() {
        const moderationSystemPrompt = `You are a moderation assistant. Your role is to detect content about {domain} in the text provided, and mark the severity of that content.

        ## {domain}
        
        ### Criteria
        
        {scoring_criteria}
        
        ### Instructions
        
        {scoring_steps}
        
        ### Content
        
        {content}
        
        ### Evaluation (score only!)`;
      
        const modMessages = [
            {
                "role": "user",
                "content": moderationSystemPrompt.replace('{domain}', domain)
                                                  .replace('{scoring_criteria}', dental_health_criteria)
                                                  .replace('{scoring_steps}', dental_health_steps)
                                                  .replace('{content}', chatResponse)
            },
        ];

        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${openaiApiKey}`
            },
            body: JSON.stringify({
                model: "gpt-4o-mini",
                messages: modMessages,
                temperature: 0
            })
        });

        if (!response.ok) {
            throw new Error('HTTP error! status: ' + response.status);
        }

        const data = await response.json;
        
        return data.choices[0].message.content;
    }

    try {
        const moderationResponse = await checkOutputGuardrail();
        const score = parseInt(moderationResponse, 10);
        let message;
        if (score >= 3) {
            message = `Moderation guardrail flagged with a score of ${score}.`;
            return {
                next: { path: 'moderation_triggered' },
                trace: [{ type: "debug", payload: { message } }],
                output: { message, score }
            };
        } else {
            message = "Passed moderation.";
            return {
                next: { path: 'continue' },
                trace: [{ type: "debug", payload: { message } }],
                output: { message, score }
            };
        }
    } catch (error) {
        return {
            next: { path: 'error' },
            trace: [{ type: "debug", payload: { message: `Error in moderation guardrail: ${error.message}` } }]
        };
    }
}

// Just the output with three paths: moderation_triggered, continue, and error.
export default async function main(args) {
    const { openaiApiKey, chatResponse } = args.inputVars;

    if (!chatResponse || !openaiApiKey) {
        return {
            next: { path: 'error' },
            trace: [{ type: "debug", payload: { message: "Missing required input variable: chatResponse or openaiApiKey" } }]
        };
    }

    const url = `https://api.openai.com/v1/chat/completions`;
    const domain = "pediatric dentistry and children's dental health";
    const dental_health_criteria = `
    Assess the presence of misinformation, harmful advice, or non-related content in the context of pediatric dentistry and children's dental health.
    The content should:
    1. Contain accurate and safe advice about pediatric dentistry and children's dental health.
    2. Be relevant to pediatric dentistry and children's dental health.`;
    const dental_health_steps = `
        1. Read the content and the criteria carefully.
    2. Assess how much misinformation, harmful advice, or non-related content is contained in the content.
    3. Assign a dental health score from 1 to 5, with 1 being no misinformation, harmful advice, or non-related content, and 5 being multiple instances of misinformation, harmful advice, or non-related content.`;

    async function checkOutputGuardrail() {
        const moderationSystemPrompt = `You are a moderation assistant. Your role is to detect content about {domain} in the text provided, and mark the severity of that content.

        ## {domain}
        
        ### Criteria
        
        {scoring_criteria}
        
        ### Instructions
        
        {scoring_steps}
        
        ### Content
        
        {content}
        
        ### Evaluation (score only!)`;
      
        const modMessages = [
            {
                "role": "user",
                "content": moderationSystemPrompt.replace('{domain}', domain)
                                                  .replace('{scoring_criteria}', dental_health_criteria)
                                                  .replace('{scoring_steps}', dental_health_steps)
                                                  .replace('{content}', chatResponse)
            },
        ];

        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${openaiApiKey}`
            },
            body: JSON.stringify({
                model: "gpt-4o-mini",
                messages: modMessages,
                temperature: 0
            })
        });

        if (!response.ok) {
            throw new Error('HTTP error! status: ' + response.status);
        }

        const data = await response.json;
        
        return data.choices[0].message.content;
    }

    try {
        const moderationResponse = await checkOutputGuardrail();
        const score = parseInt(moderationResponse, 10);
        let message;
        if (score >= 3) {
            message = `Moderation guardrail flagged with a score of ${score}.`;
            return {
                next: { path: 'moderation_triggered' },
                trace: [{ type: "debug", payload: { message } }]
            };
        } else {
            message = "Passed moderation.";
            return {
                next: { path: 'continue' },
                trace: [{ type: "debug", payload: { message } }]
            };
        }
    } catch (error) {
        return {
            next: { path: 'error' },
            trace: [{ type: "debug", payload: { message: `Error in moderation guardrail: ${error.message}` } }]
        };
    }
}


/*
Here are some example questions to thoroughly test your moderation function, including edge cases:

1. **Accurate Information:**
   - "What are the benefits of fluoride treatments for children's teeth?"
   - "How often should children visit the dentist for checkups?"

2. **Potential Misinformation:**
   - "Is it true that baby teeth don't need to be brushed because they fall out anyway?"
   - "I've heard that chewing gum can replace brushing. Is this correct for children?"

3. **Harmful Advice:**
   - "Can I use adult toothpaste for my toddler?"
   - "Is it safe to give my child sugary snacks before bedtime if they brush their teeth afterward?"

4. **Neutral/General Questions:**
   - "What is the best way to make a dental appointment at your clinic?"
   - "Can you tell me about your clinic's hours of operation?"

5. **Edge Cases:**
   - "How can I soothe my child's teething pain without using any medication?"
   - "Is it okay to use a hard-bristled brush on my child's teeth to clean them better?"
   - "Are there any home remedies for treating cavities in children?"

6. **Explicit Misinformation:**
   - "I've read that it's okay to skip brushing if my child uses mouthwash daily. Is this true?"
   - "Do children's teeth naturally clean themselves, so brushing is unnecessary?"

7. **Unclear or Ambiguous Questions:**
   - "What should I do if my child hates the taste of toothpaste?"
   - "How important is flossing for kids, and when should they start?"

8. **Questions with Mixed Information:**
   - "Is it safe to use over-the-counter whitening strips on my child's teeth if they have stains?"
   - "Can children use the same mouthwash as adults, or should they use a special one?"

9. **Non-Related Questions:**
   - "What are the best breeds of dogs for families with kids?"
   - "Can you recommend a good vet for my cat?"

10. **Borderline Content:**
    - "Is it true that certain diets can prevent cavities in children?"
    - "Can essential oils help improve my child's dental health?"

These questions cover a range of scenarios, from general inquiries to potentially harmful misinformation, ensuring your moderation function can accurately assess and flag inappropriate or unsafe content.

*/