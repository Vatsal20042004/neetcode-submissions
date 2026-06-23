class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for ele in nums:
            if ele in freq:
                freq[ele]+=1
            else:
                freq[ele]=1
        minheap=[]
        for ele,f in freq.items():
            heapq.heappush(minheap,(f,ele))

            if len(minheap)>k:
                heapq.heappop(minheap)
        res=[]
        for f,ele in minheap:
            res.append(ele)
        
        return res
        