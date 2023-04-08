## Discussion Questions

1. [Difference between LLMs](#a1) <span id="q1"></span>
2. [Finding clusters K means — Are You Still Using the Elbow Method?](#a2) <span id="q2"></span> 
3. [ML model deployment](#a3) <span id="q3"></span>
4. [ChatGPT era - reinvent yourself](#a4) <span id="q4"></span>
5. [Maths for ML/DS/DL/AI](#a5) <span id="q5"></span>
6. [Transformer Study and Tutorials](#a6) <span id="q6"></span>



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

[LLMs ain't what you think they are](https://www.linkedin.com/posts/activity-7027970160925847552-wydr)

♠ ChatGPT is dumb for computation. 
♥ LLMs suck at even the basic arithmetic and logic.
♦ Scale is not the answer, and, even if it was, it would be a wasteful one.
♣ Computing increasingly more statistics over the whole internet might give you an awesome search assistant or a quirky chat pal (in a positive way 😜 ), but that's about it, regardless how you package it.

A few quotes to support the claims:
♠ https://lnkd.in/d-q_wmjm - Language Models are Few-Shot Learners - GPT-3 can barely do 3-digit integer addition and subtraction and fails with more digits.
♥ https://lnkd.in/dcTEtYaX Mathematical Capabilities of ChatGPT: "We conclude that contrary to many positive reports in the media (a potential case of selection bias), ChatGPT’s mathematical abilities are significantly below those of an average mathematics graduate student. Our results show that ChatGPT often understands the question but fails to provide correct solutions"
♦ And finally, here is a single-neuron 2-parameter model in PyTorch that outperforms 175B-parameter GPT-3 in arbitrary addition (even with floating point numbers). https://lnkd.in/dgnHRf2K. A similar model with a change of just one parameter can do arbitrary subtraction.

🤔 So why didn't one of those billions of neurons learn to do addition? (this rabbit-hole is rather a funny one, but in the meantime, let's stop feeding fuel to the hype) 

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

---

 [Standardizing the Machine Learning Lifecycle From experimentation to production with MLflow by Databricks](https://www.linkedin.com/posts/ashishpatel2604_mlflow-by-databricks-ugcPost-7028370034502569984-wKd4/)[file](/ml_study/files/ml_lifecycle_databricks.pdf)  
 Standardizing the Machine Learning Lifecycle From experimentation to production with MLflow by Databricks

Chapters Catalogue:

⚡Machine LearningLifecycle Challenges
⚡Applying Good EngineeringPrinciples to Machine Learning
⚡Introducing MLflow
⚡A Closer Look at MLflowModel Registry
⚡Making OrganizationsSuccessful with ML
⚡Introducing the UnifiedData Analytics Platform
⚡Standardizing the MachineLearning Lifecycle on Databricks
⚡Getting Started
⚡Comparison Matrix

--- 

Building models used to be the "exciting" part of data science.

Nowadays, I usually consider that solved.

What isn't solved is the data:

Take AutoML as an example.

Modern AutoML platforms abstract and automate large parts of the supervised machine learning workflow, including:

- Finding the best algorithm
- Finding the best training parameters
- Optimising the features (feature engineering)
- Splitting your data into training & test sets
- Deploy your model & monitor performance

What AutoML does not solve is the following:

- Finding the right use case
- Collect the right data
- Prepare the data
- Define features

So what does this mean?

If you're a 'data expert' in your organisation (hello, BI folks!), chances are you can challenge even seasoned data scientists by leveraging your data and domain expertise combined with very basic machine learning skills.

This could easily boost your career.

And you don't have to wait for anyone's permission to build your ML portfolio. It's up to you.

---

* __ChatGPT era - reinvent yourself__[#](#q4) <span id="a4"></span>

[Staying relevant in the (post-) ChatGPT era. A few pointers for students.](https://www.linkedin.com/posts/ramgopalrao_chatgpt-activity-7027890077586366466-uCSd) 

I used to tell students that, if they aren't creative, Google will replace them. Now with #ChatGPT on the horizon, and having used it for a few months now, I tell them, even if you are creative, there is a possibility that ChatGPT may replace you.

So what do you do to stay relevant?

Here are my 5 pointers. You may add more.

1. Continuous learning and upgradation of skills is very important. Half shelf life of knowledge is becoming shorter and shorter. Learn to use new tools like ChatGPT effectively to boost your personal and group's productivity. Just as you don't hire a driver who can't use Google Maps, no company will hire you in the future if you can't use these tools effectively. Always remember, technology can be a useful servant but a dangerous master.

2. Innovation will thrive in the days to come. Innovation is going beyond creativity. Innovation is about generating value for your ideas. There is enough evidence to suggest that your connections and networks are more important for innovation than your knowledge and creativity. So network with people coming from different cultures, attitudes and backgrounds. Don't be a cocoon.

3. Never be shallow and casual about anything you do. If your job is getting too routine, too comfortable and if you aren't learning anything new, believe me, the job isn't going to last long.

4. Learn to be an effective team player. In a team, always remember, what matters the most is how good you are for the team than your own individual excellence.

5. When you decide on any career path, don't fall for the salary packages or the FOMO factors. Decide with your heart, but let the mind takeover and do all the planning next. As a famous poet once said, let your desires be guided by heart, and the achievements by your mind. If you take all your decisions by your mind, you may never find your passion and may never do anything great. If you always let your heart to decide, you may not be able to deal with the repercussions. As the saying goes, when you find your passion, you will find your purpose. Heart-Mind coordination is essential for this.

V Ramgopal Rao, IIT Delhi 

[Will prompting the LLM to review it's own answer be any helpful to reduce chances of hallucinations?](https://www.reddit.com/r/MachineLearning/comments/123b4f0/d_will_prompting_the_llm_to_review_its_own_answer/)

---

* __Maths for ML/DS/DL/AI__[#](#q5) <span id="a5"></span>

* [What's the most advanced mathematics you have used in your job as a data scientist?](https://www.quora.com/Whats-the-most-advanced-mathematics-you-have-used-in-your-job-as-a-data-scientist)

__Books__
*[Readme Books](/ml_study/books/review.md#ml_books)


---
__Transformer Study and Tutorials__
* [Resources for Understanding The Original Transformer Paper](https://www.reddit.com/r/MachineLearning/comments/pkedi4/d_resources_for_understanding_the_original/)
* [What is a good beginner tutorial on transformers and how they work with question answering models from hugging face?](https://www.reddit.com/r/learnmachinelearning/comments/sw1kj9/what_is_a_good_beginner_tutorial_on_transformers/)
* [ChatGPT and Transformers study] (https://www.reddit.com/r/learnmachinelearning/comments/123fcrq/i_tried_to_get_a_grasp_of_llms_using_chatgpt_im/):
Linear Algebra by Friedberg Insel and Spence
Differential and Integral Calculus by Richard Courant
Elements of Statistical Learning
Those three on theory are a good place to start for foundation.
What is ChatGPT Doing by Stephen Wolfram.
Natural Language Processing with Transformers by Tunstall, Werra and Wolf.
Any of the Grokking series.