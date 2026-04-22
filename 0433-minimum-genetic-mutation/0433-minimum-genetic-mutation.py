class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        queu = deque([(startGene, 0)])
        vistied = set([startGene])
        bank = set(bank)
        while queu:
            gene, count = queu.popleft()

            for i in range(len(gene)):
                for c in ["A","C","G",'T']:
                    new_word = gene[:i] + c + gene[i+1:]

                    if new_word == endGene:
                        return count + 1
                    if new_word in bank and new_word not in vistied:
                        vistied.add(new_word)
                        queu.append((new_word, count+1))
        
        return -1
