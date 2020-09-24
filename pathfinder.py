def backTrack(target, word, node, graph, path=[]):
    if len(word) == 0:
        formedWord = ''    
        for _ in path:
            formedWord += _.character
        if formedWord == target:
            return path
        return False
            
    adjacencyList = graph[node]
    adjacencyCharacterList = [x.character for x in adjacencyList]
    if word[0] in adjacencyCharacterList:
        indexes = [x for x in range(len(adjacencyCharacterList)) if adjacencyCharacterList[x] == word[0]]
        for i in indexes:
            if adjacencyList[i] not in path:
                newPath = path.copy()
                newPath.append(adjacencyList[i])
                return backTrack(target, word[1:], adjacencyList[i], graph, newPath)
    return False

def validateWord(board, word):    
    roots = board.getInstances(word[0])    
    for root in roots:
        res = backTrack(word, word[1:], root, board.adjacencyList, [root])

        if res != False:
            return res
            # img = drawPath(IMG, res, RED)
            # showImage('', img)
            # print(res)
    return False

                
if __name__ == '__main__':
    import pickle
    with open('sample_board.dat', 'rb') as file:
        board = pickle.load(file)
    
    # dfs([], board.adjacencyList, board.board[1][0])
    res = validateWord(board, "ROSEY")
    print(res)