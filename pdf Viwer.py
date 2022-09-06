def designerPdfViewer(h, word):
    height=[]
    idx=0
    for ch in word:
        idx=ord(ch)-97
        height.append(h[idx])
    return max(height)*len(word)

h=[1 ,3 ,1 ,3 ,1, 4 ,1 ,3 ,2 ,5 ,5 ,5, 5, 5, 5 ,5 ,5 ,5, 5 ,5, 5 ,5 ,5 ,5 ,5 ,7]
word='zaba'
print(designerPdfViewer(h,word))