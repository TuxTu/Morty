from morty.morty import Morty

# Define model path the parameters
llama_path = "models/llama-2-7b-chat/ggml-model-Q4_K_M.gguf"
claude_api = "api/claude.txt"

params = {
    "max_tokens": 2048,
    "temperature": 0.3,
    "top_p": 0.1,
    "stop": ["Q", "\n"]
}

if __name__ == "__main__":
    # morty = Morty(llama_path, params, "llama")
    morty = Morty(claude_api, params, 'claude')
    morty.listen()
