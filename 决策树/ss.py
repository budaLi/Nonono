#判定树是一种类似于流程图的树结构 其中每个内部节点表示在一个属性上的
# 测试，每个分支表示一个属性输出，而每个树叶节点代表类或者类分布，树的最
# 顶层是根节点。
#信息熵 H(x)=∑F(x)log2(F(x))  变量的不确定性越大 信息熵越大
#决策树归纳算法 ID3


import tensorflow as tf
word = tf.constant("hello")
sess = tf.compat.v1.Session()
print(sess.run(word))