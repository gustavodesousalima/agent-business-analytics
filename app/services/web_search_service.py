from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

def search_web(query):
    result = search_tool.run(query)
    print(result)
    return result