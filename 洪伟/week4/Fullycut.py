#week4作业
#参考了宋老师的代码

#词典；每个词后方存储的是其词频，词频仅为示例，不会用到，也可自行修改
Dict = {"经常":0.1,
        "经":0.05,
        "有":0.1,
        "常":0.001,
        "有意见":0.1,
        "歧":0.001,
        "意见":0.2,
        "分歧":0.2,
        "见":0.05,
        "意":0.05,
        "见分歧":0.05,
        "分":0.1}

def calc_dag(sentence):
        DAG = {}  
        N = len(sentence)
        for k in range(N):
            tmplist = []
            i = k
            frag = sentence[k]
            while i < N:
                if frag in Dict:
                    tmplist.append(i)
                i += 1
                frag = sentence[k:i + 1]
            if not tmplist:
                tmplist.append(k)
            DAG[k] = tmplist
        return DAG


class DAGDecode:
    def __init__(self,sentence):
        self.sentence = sentence
        self.DAG = calc_dag(sentence)
        self.len = len(sentence)
        self.code_path = [[]]
        self.decode_path = []
    
    def decode_next(self,path):
        path_len = len("".join(path))
        if path_len == self.len:
            self.decode_path.append(path)
            return
        
        Containers = self.DAG[path_len]
        new_paths = []
        for sample in Containers:
            new_paths.append(path + [self.sentence[path_len:sample + 1]])
        self.code_path += new_paths
        
    def decode(self):
        while self.code_path != []:
            path = self.code_path.pop()
            self.decode_next(path)

    
sentence = "经常有意见分歧"
dd = DAGDecode(sentence)
dd.decode()
print(dd.decode_path)