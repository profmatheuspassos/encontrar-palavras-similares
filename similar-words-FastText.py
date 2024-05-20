import os
import gensim
import gensim.downloader as api

# Diretório onde o modelo será salvo
MODEL_DIR = "models"
# Caminho completo para o arquivo do modelo
MODEL_PATH = os.path.join(MODEL_DIR, "fasttext-wiki-news-subwords-300")

def load_or_download_model():
    # Verificar se o diretório do modelo existe; se não, criar
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)
    
    # Verificar se o modelo já foi salvo localmente
    if os.path.exists(MODEL_PATH):
        print("Carregando modelo local...")
        model = gensim.models.FastText.load(MODEL_PATH)
    else:
        print("Baixando o modelo FastText pré-treinado...")
        model = api.load("fasttext-wiki-news-subwords-300")
        print("Modelo baixado com sucesso! Salvando localmente...")
        model.save(MODEL_PATH)
    return model

def get_similar_words(model, word):
    if word in model.key_to_index:
        similar_words = model.most_similar(word)
        return similar_words
    else:
        return None

def main():
    model = load_or_download_model()
    while True:
        user_input = input("Digite uma palavra (ou 'fim' para terminar): ").strip()
        if user_input.lower() == 'fim':
            break
        similar_words = get_similar_words(model, user_input)
        if similar_words:
            print(f"Palavras semelhantes a '{user_input}':")
            for word, similarity in similar_words:
                print(f"  {word} (similaridade: {similarity:.4f})")
        else:
            print(f"A palavra '{user_input}' não foi encontrada no modelo.")

if __name__ == "__main__":
    main()
