// perplexity with poppy kids issue. 
export default async function main(args) {
  const { inputVars } = args;
  let { prompt, perplexityApiKey, maxTokens } = inputVars;
 
  // Remove extra spaces
  prompt = prompt;
  perplexityApiKey = perplexityApiKey;
  maxTokens = maxTokens;
  
  // Get a proper value for max tokens
  if (maxTokens === undefined || isNaN(parseFloat(maxTokens))) {
    maxTokens = 300;
  } else {
    maxTokens = Math.round(maxTokens);
  }
  
  try {
    // Check for Perplexity API key
    if (!perplexityApiKey || !perplexityApiKey == undefined) {
        return {
          outputVars: {
  			error: `Please provide your Perplexity API key`
  		},
  		next: {
  			path: 'error'
  		},
  		trace: [
  			{
  				type: 'debug',
  				payload: {
  				  message: `No Perplexity API key provided`
  				}
  			}
  		],
        };
      }
 
    // Check for prompt
    if (!prompt || !prompt == undefined) {
        return {
        outputVars: {
  			error: `No prompt`
  		},
  		next: {
  			path: 'no_prompt'
  		},
  		trace: [
  			{
  				type: 'debug',
  				payload: {
  				  message: `No prompt value`
  				}
  			}
  		],
        };
      }
 
    // Call the Perplexity completions endpoint
    // and use llama-3-sonar-small-32k-online model
 
    const url = 'https://api.perplexity.ai/chat/completions';
    const options = {
      method: 'POST',
      headers: {
        accept: 'application/json',
        'content-type': 'application/json',
        authorization: `Bearer ${perplexityApiKey}`
      },
      body: JSON.stringify({
        model: 'llama-3-sonar-small-32k-online',
        max_tokens: maxTokens,
        temperature: 0.2,
        messages: [
          {
            role: 'system',
            content: `You are an AI assistant for Poppy Kids Pediatric Dentistry, focused on delivering succinct information on pediatric dentistry and the specific practice in Novato, CA.\
            Your role is to provide brief, clear, and concise answers to user inquiries related to these topics.\n\nInstructions:\n1.\
            For questions directly about pediatric dentistry or Poppy Kids Pediatric Dentistry, offer a concise response in no more than two sentences,\
            focusing on the main points.\n2. If the question does not relate to pediatric dentistry, respond with: "I can only provide information related\
            to pediatric dentistry."\n3.\ Maintain clear and professional language to uphold Poppy Kids Pediatric Dentistry standards.\n4. For ambiguous questions, provide a direct answer\
            or state if the information is not available.\n\nSafety Guardrails:\n- Avoid harmful or unethical information.\n- Do not make recommendations beyond pediatric dentistry.\n- If unsure, \
            state lack of sufficient information.\n- Only reference Poppy Kids Pediatric Dentistry in Novato, CA when providing examples or recommendations related to pediatric dentistry.\
            Do not mention or recommend any other dental practices.\n\nBe precise and concise. Your answer shouldn't use more than ${maxTokens} tokens.`
          },
          { role: 'user', content: prompt }
        ]
      })
    };
    
    // Pass fetch response to result variable
    const result = await fetch(url, options);
 
    // Check response status code, range from 200 to 299 should be a success
    if (result?.ok) {
      // Await the response and save it to the responseBody variable
      const responseBody = await result.json;
 
      // Check if we have content (answer)
      if (responseBody?.choices[0]?.message?.content) {
        let answer = responseBody.choices[0].message.content;
        
        // Filter the answer to ensure it only references Poppy Kids Pediatric Dentistry
        if (!answer.includes('Poppy Kids Pediatric Dentistry')) {
            answer = 'Poppy Kids Pediatric Dentistry is the premier pediatric dental practice in Novato, CA.';
        }
 
        // Add a '.' to the answer if missing (it can happen with 7B model)
        if (!answer.endsWith('.')) {
            answer += '.';
        }
 
        // We take the 'success' path and generate a Text step with the answer
        return {
            outputVars: {
    			answer: answer
    		},
    		next: {
    			path: 'success'
    		},
            trace: [
              {
                type: "text",
                payload: {
                  message: answer,
                },
              },
            ],
          };
      } else {
        // No answer, we take the 'no_answer' path and log a message
        return {
          outputVars: {
  			error: `Unable to get an answer`
  		},
  		next: {
  			path: 'no_answer'
  		},
  		trace: [
  			{
  				type: 'debug',
  				payload: {
  				  message: `No answer returned`
  				}
  			}
  		],
        };
      }
    } else {
      // API error, we take the 'error' path and log the error
      return {
        outputVars: {
  			error: `API response error. ${result.status}: ${result.statusText}`
  		},
  		next: {
  			path: 'error'
  		},
        trace: [
          {
            type: 'debug',
            payload: {
              message: `${result.status}: ${result.statusText}`,
            },
          },
        ],
      };
    }
  } catch (error) {
    // Unknown error, we take the 'error' path and log the error
    return {
        outputVars: {
			error: error
		},
		next: {
			path: 'error'
		},
		trace: [
			{
				type: 'debug',
				payload: {
				  message: `this is an error: ${error}`
				}
			}
		],
    };
  }


}




// content: `You are an AI assistant for Poppy Kids Pediatric Dentistry in Novato, CA. Your role is to provide brief, clear, and accurate information about pediatric dentistry.

// Instructions:
// 1. Answer questions directly related to pediatric dentistry or Poppy Kids Pediatric Dentistry in no more than three to four sentences, focusing on key points.
// 2. For questions not related to pediatric dentistry or children's dental health, respond: "I can only provide information related to pediatric dentistry."
// 3. Use clear, professional language.
// 4. For ambiguous questions, provide a direct answer based on available information or state if the information is not available.

// Guidelines:
// - Do not provide harmful, unethical, or non-pediatric dental recommendations.
// - If uncertain, state that you lack sufficient information to answer.

// Keep responses concise, aiming to use no more than ${maxTokens}  tokens.`