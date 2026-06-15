import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentResponse,Content,Part

def print_token_information(response: GenerateContentResponse):
    if response is None:
        raise RuntimeError("Response metdata is None mostly your API call failed")
    prompt_token_count = response.usage_metadata.prompt_token_count
    response_token_count = response.usage_metadata.candidates_token_count
    print(f"Prompt tokens: {prompt_token_count}")
    print(f"Response tokens: {response_token_count}")



def main():
    load_dotenv()
    args_parser = argparse.ArgumentParser(description="ChatBot")
    args_parser.add_argument("user_prompt",type=str,help="User prompt")
    args_parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = args_parser.parse_args()
    messages: list[Content] = [
        Content(role="user",parts=[Part(text=args.user_prompt)])
    ]
    api_key = os.environ.get("GEMINI_API_KEY")
    client  = genai.Client(api_key=api_key)
        
    response = client.models.generate_content(model="gemini-2.5-flash",contents=messages)
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print_token_information(response)
    else:
        print(response.text)





if __name__ == "__main__":
    main()
