# BGP-Analyzer
A simple Analyzer for BGP route data from RouteView project.

## Data Source
[Route Views Project](http://www.routeviews.org/)

## AS Data Analyze
以2014-07-27 8-10点收集的BGP路由数据来看，共有47924个自制域(AS)、522123个前缀(prefix)。
![Imgur](http://i.imgur.com/ALvpu1U.png)

### AS前缀的分布
![Imgur](http://i.imgur.com/dvzVOfB.png)

取对数稍加处理

![Imgur](http://i.imgur.com/nBLcT3Y.png)

两者取对数之后，总体来看成线性关系，即当IP前缀增长时，对应的AS数量成指数下降

### AS前缀中IP数量的分布
![Imgur](http://i.imgur.com/3dAHxAQ.png)

取对数处理

![Imgur](http://i.imgur.com/CXL0sP8.png)

取对数后两者的线性关系也不是特别明显，而是出现分块现象，这可能是由于A、B、C类地址数量差异较大造成

### AS节点度的分布
![Imgur](http://i.imgur.com/b4IDm1Z.png)

这是自治域号与其节点对应的分布关系，从图中可以得出一些简单的结论，早期申请的AS节点度普遍较高，取对数处理
![Imgur](http://i.imgur.com/2txcgKX.png)

从上图可以看出随着节点的增大，自治域的数量成指数减小，这个结果也符合实际情况。

### AS节点度与声明前缀的取对数关系图
![Imgur](http://i.imgur.com/U160Qyw.png)

从上图看不出明显的函数关系，所以做一下分组处理，得到下图
![Imgur](http://i.imgur.com/0nFlkQD.png)

从上图可以看出，分组合并之后，随着节点度的增大，前缀成指数倍减少，这和实际情况也是相符的。节点度大的前缀数量少，但是每个前缀包含的IP数量多