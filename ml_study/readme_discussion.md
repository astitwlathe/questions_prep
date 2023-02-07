## Discussion Questions

1. [Difference between LLMs](#a1) <span id="q1"></span>
2. [Finding clusters K means — Are You Still Using the Elbow Method?](#a2) <span id="q2"></span> 
3. [ML model deployment](#a3) <span id="q3"></span>


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

---

* __Elbow, BIC, etc. methods for finding clusters__[#](#q2) <span id="a2"></span>

[Are you still using the "elbow method"?](https://towardsdatascience.com/are-you-still-using-the-elbow-method-5d271b3063bd)

Despite being so popular, the elbow method is pretty much the worst choice one can do when choosing the number of clusters for a dataset.

So what should you use instead?

In a recent paper, Erich Schubert shows that BIC (Bayesian Information Criterion) often outperforms other methods. So, I have taken the GoLang implementation of BIC made by Robert Hancock, translated it into Python, and tested it against the elbow method.

The difference in performance between the two methods is huge!

For example, in these 5 datasets, the elbow method guesses the true number of clusters only once, whereas the BIC score makes the right choice every time.

☕ Read about the full experiment in my article on Towards Data Science: https://lnkd.in/dEpMjpBP

🐍 Find the fully reproducible Python code on my GitHub: https://lnkd.in/dxvAq6Jg

---

* __ML model deployment__[#](#q3) <span id="a3"></span>

[Why is deploying a machine learning model so hard](https://www.linkedin.com/posts/iamabhishekchoudhary_why-is-deploying-a-machine-learning-model-activity-7027683050654187520-_8kd)   
First, it's not about using a tool!
⚡ Every model consumer is different
💥 Resource utilization varies a lot & hard to predict ahead
🕵️ Debugging live model in Production is not easy
🔥 Data drift can be a silent killer and figuring that out automatically is a hard problem

✔️ The model may have some bad code which can cost resources or unknown performance

🚧 A/B testing to production timeline is highly debatable & figuring out organic vs non organic growth takes time.