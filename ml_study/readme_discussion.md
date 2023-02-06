## Discussion Questions

1. [Difference between LLMs](#a1) <span id="q1"></span>



<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />



* __Difference between LLMs__[#](#q1) <span id="a1"></span>

[LLMs, Microsoft partnership](https://www.linkedin.com/feed/update/urn:li:activity:7025864120314863616/)
As a preamble, the number of significant modifications you have to do in inits, pre-norm, reverse tokenization... Choices you have to make in numerical stability for casual vs non-causal vs ED... Model changes you have to make for FLM vs Prefix-LM vs Masked on the objective side..... Multi-task query modification, changes in adaptations, Sparsity, Parallelization... I can go on....

Each LLMs has such vast innovations and they are not just parameter and data. They are in no way similar.

What are the effect of all the transformations vs the scale? Would the models be behaving vastly differently with or without those changes? It feels they are added just to be able to say "our models are somewhat different". There is never an ablation study on the "drastic effect" of those changes.

There are truck loads of studies and articles on how the stated innovations reduce the number of parameters needed to actually outperform larger models (As one example). With simple search you can find them on your own in Arxiv  ;)

For example, you will see how Alexa TM (Teacher Model) with a 20B parameter outperforms GPT3 which is a 175B model.
