# PyMC Labs Blog Posts Summary

Generated: 2025-11-07 12:27:00
Total Posts: 63

---

## 1. Stochastic Volatility Model with PyMC

**URL:** https://www.pymc-labs.com/blog-posts/01-xpost-tw-stochastic-volatility

**Description:** Explore the concept of time-varying volatility in asset prices, modeled using a stochastic process. The example demonstrates the computation of this volatility based on the daily returns of the S&P 500 using PyMC.

**Word Count:** 0

**File:** `001_01-xpost-tw-stochastic-volatility.txt`

**Summary:**

No content available.

---

## 2. MCMC sampling for dummies

**URL:** https://www.pymc-labs.com/blog-posts/02-xpost-tw-MCMC-sampling

**Description:** Explore the intuition behind MCMC sampling and the random-walk Metropolis algorithm through code examples rather than complex formulas or math-speak.

**Word Count:** 129

**File:** `002_02-xpost-tw-mcmc-sampling.txt`

**Summary:**

MCMC sampling for dummies September 23, 2025 ByThomas Wiecki How is inference actually performed and how does it work? How do we get these magical samples from the posterior? The beauty of probabilistic programming is that you actually don't have to understand how the inference works in order to build models, but it certainly helps. Math and statisics tend to seem complex because when they are taught, no one ever tells you about the intuition behind the concepts (which is usually quite simple) but only hands you some scary math. This blog post is an attempt at trying to explain the intuition behind MCMC sampling (specifically, the random-walk Metropolis algorithm). Critically, we'll be using code examples rather than formulas or math-speak. For the full example, see:MCMC sampling for dummies

---

## 3. NBA Foul Analysis with Item Response Theory using PyMC

**URL:** https://www.pymc-labs.com/blog-posts/03-xpost-ar-nba-irt

**Description:** Delve into the use of Bayesian Item Response Theory and the Rasch model for analyzing NBA foul calls data. The model estimates individual player contributions to foul outcomes.

**Word Count:** 0

**File:** `003_03-xpost-ar-nba-irt.txt`

**Summary:**

No content available.

---

## 4. Building Time-Series Models With Known Data Structure

**URL:** https://www.pymc-labs.com/blog-posts/04-xpost-be-time-series-volcano

**Description:** Dive into the application of Gaussian Processes in constructing time-series models, leveraging domain knowledge of the underlying time-series. The discussion includes the use of PyMC for modeling carbon dioxide measurements derived from ice cores and atmospheric readings from Mauna Loa, a Hawaiian volcano.

**Word Count:** 0

**File:** `004_04-xpost-be-time-series-volcano.txt`

**Summary:**

No content available.

---

## 5. PyMC, Aesara and AePPL: The New Kids on The Block

**URL:** https://www.pymc-labs.com/blog-posts/2022-07-10-ricardo-video

**Description:** Dive into the world of PyMC, Aesara, and AePPL, the new powerhouses in probabilistic programming. Discover how they revolutionize Bayesian modeling and open up new possibilities for data analysis.

**Word Count:** 10554

**File:** `005_2022-07-10-ricardo-video.txt`

**Summary:**

PyMC, Aesara and AePPL: The New Kids on The Block September 23, 2025 ByRicardo Vieira Introduction In July, 2022, PyMC Labs hosted a talk about PyMC, Aesara, and AePPL: the new kids on the block. Ricardo Vieira explored the inner workings of the newly released version of PyMC (v 4.0). He looked at the Aesara backend, focusing on the brand newRandomVariableoperators, which are the foundation of PyMC models. He then talked about a self-contained PPL project (Aeppl) dedicated to converting Aesara RandomVariable graphs to probability functions and then, how PyMC makes use of these two packages to create efficient random generator functions and probability evaluation functions, with the ultimate goal of facilitating a fully-fledged modern Bayesian workflow. PyMCis a probabilistic programming library for Python that allows users to build Bayesian models with a simple Python API and fit them using Markov chain Monte Carlo (MCMC) methods. Aesarais a Python library that allows users to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently. Aesara is based on Theano (https://github.com/Theano/Theano), which has been powering large-scale computationally intensive scientific investigations since 2007. AePPLis a new library focused on converting (arbitrary) graphs containing Aesara RandomVariables into joint log-probability graphs. It can understand complex graphs that include nested operations, conditionals, loops, and advanced indexing, allowing one to generate rich probability functions automatically without having to muddle through the mathematical details. About Speaker Ricardo Vieira is a PyMC developer and data scientist at PyMC Labs. He spent several years teaching himself Statistics and Computer Science at the expense of his official degrees in Psychology and Neuroscience. GitHub:https://github.com/ricardoV94/ Twitter:https://twitter.com/RicardoV944 Website:https://ricardov94.github.io/posts/ Resources PyMC V4 Release announcement PyMC V4 Release notes PyMC website About Aesara About Aeppl Outline Introduction Aesara and random variables AePPL and probabilities PyMC and the modern Bayesian workflow Q&A The timestamps below provide...

---

## 6. Bayesian Modeling in Biotech: Using PyMC to Analyze Agricultural Data

**URL:** https://www.pymc-labs.com/blog-posts/2022-08-11-indigo

**Description:** Uncover the power of Bayesian modeling in biotechnology. Learn how PyMC is used to analyze complex agricultural data, providing valuable insights for the industry.

**Word Count:** 310

**File:** `006_2022-08-11-indigo.txt`

**Summary:**

Bayesian Modeling in Biotech: Using PyMC to Analyze Agricultural Data September 23, 2025 ByThomas Wiecki Introduction In July 2022, we organized a panel discussion with Manu Martinet ofIndigo Agand Thomas Wiecki and Bill Engels of PyMC Labs to discuss a case-study of measuring effects of crop-types in an agricultural setting. The goal of the project was to identify the underlying spatial pattern and remove it in order to measure more accurately the treatment effect, which in this case are microbes which contribute to plant yield. PyMC Labs were consultants on this project which had limited data and which used Bayesian analyses and Gaussian processes to identify the treatment effect. We demonstrate how Bayesian modeling is a powerful tool for solving problems in biotechnology. Timestamps 00:00Thomas Wiecki does PyMC introduction 02:49Thomas introduces self 03:33Manu Martinet introduces self 04:25Bill Engels introduces self 05:10Panel discussion begins 06:51Testing crop yields on fields 08:16How do you sell the product to farmers? 10:55Data modeling and challenges 13:04Goal of the project: Estimate the spatial pattern and remove it to get the treatment effect 15:20Gaussian processes and how they are used 18:04Spatial Gaussian Processes 19:09Spatial effects 22:13Examples fields to show the spatial components 24:28Question: How does modeling the spatial component with a Guassian process compare with other simpler methods? 25:47Question: With the Gaussian Process(GP) can you estimate the spatial scale? 28:06Question: How does the Gaussian Process deal with latent variables? 30:08Advantages of the a Bayesian framework 35:00Collaboration between Indigo and PyMC Labs review 42:43Question: What were the biggest challenges in the study? 45:29Question: Is there any example online for PyMC based Hierarchical Gaussian Processes(GP) regression? 46:37Question: How did the decomposition work out between signal, spatial and noise and how do you balance the confidence between what is signal and what is noise? 47:35Question: How to effectively use Bayesian...

---

## 7. Bayesian Item Response Modeling in PyMC

**URL:** https://www.pymc-labs.com/blog-posts/2022-10-26-AlvaLabs

**Description:**  Uncover the power of Bayesian Item Response Theory in PyMC. Learn how it revolutionizes data analysis and opens up new possibilities for personality modeling.

**Word Count:** 0

**File:** `007_2022-10-26-alvalabs.txt`

**Summary:**

No content available.

---

## 8. Bayesian Marketing Mix Models: State of the Art and their Future

**URL:** https://www.pymc-labs.com/blog-posts/2022-11-11-HelloFresh

**Description:** Learn the cutting-edge of Bayesian Marketing Mix Models and glimpse into their promising future. Uncover how these models are revolutionizing business strategies and decision-making processes.

**Word Count:** 0

**File:** `008_2022-11-11-hellofresh.txt`

**Summary:**

No content available.

---

## 9. Hierarchical Bayesian Modeling of Survey Data with Post-stratification

**URL:** https://www.pymc-labs.com/blog-posts/2022-12-08-Salk

**Description:** Dive into the complexities of Hierarchical Bayesian Modeling applied to survey data with post-stratification. Understand the subtleties of multilevel regression and the potential of Gaussian Processes in this comprehensive analysis.

**Word Count:** 263

**File:** `009_2022-12-08-salk.txt`

**Summary:**

Hierarchical Bayesian Modeling of Survey Data with Post-stratification September 23, 2025 ByThomas Wiecki Introduction In this panel discussion, Tarmo Jüristo tells us how Bayesian modeling can help in environments where data are noisy and uncertainty is high –like public opinion polls. In particular, data can be sparse in some strata of the population, making the model’s job harder, precisely for the demographics you’re the most interested in. A special focus is placed on the work PyMC Labs has done with Tarmo, implementing a state-of-the-art hierarchical Bayesian model. Coupled with post-stratification, this method not only makes inference possible – it makes it actionable, even you have only a few data points for some demographics. Timestamps 00:00Introduction by Thomas 03:45Tarmo introduces himself 05:20Panel discussion starts 06:11Description of Salk 08:13Zooming into the data Salk uses 10:04A look into what Tarmo does 13:58Multilevel regression with post-stratification 16:27Further refinements of the Multilevel regression with post-stratification 19:57Model output 25:50Question: On a multilevel aspect, does this mean you model other clusters/groups within other clusters/groups? 28:43Input to simulation 32:20Final simulation 34:46Alex Andorra introduces himself 36:40Question: How do you choose whether it makes sense to add interactions to a model and do you start with all possible interactions? 38:56Technical difficulties during the project 46:59Demonstration of the dashboard 51:52You can use geospatial covariation to extend the model 53:27Does the forecasting take the difference in policies between parties 54:19Using Gaussian Processes in the model(Advantages and disadvantages) 59:55Question: If you have more time, what would you add to the model 1:02:56Question: How well do you think the model is taking without rare events? 1:06:57Thank you!

---

## 10. Likelihood Approximations for Cognitive Modeling with PyMC

**URL:** https://www.pymc-labs.com/blog-posts/2023-01-12-Akili

**Description:**  Dive into cognitive modeling with PyMC. Learn about the impact of likelihood approximations.

**Word Count:** 349

**File:** `010_2023-01-12-akili.txt`

**Summary:**

Likelihood Approximations for Cognitive Modeling with PyMC September 23, 2025 ByThomas Wiecki Introduction Digital therapeutics are evidence-based, clinically evaluated software and devices that can be used to treat an array of diseases and disorders, according to the Digital Therapeutics Alliance, the industry's trade association. They can be used independently or with medications, devices, and other therapies to treat physical and behavioral health conditions, including pain, diabetes, anxiety, post-traumatic stress disorder, and asthma. In this talk,PyMC LabsandAkilidiscuss using Bayesian methods and PyMC to test a range of computational models of cognition, specifically with an eye towards ADHD (Attention-deficit/hyperactivity disorder). They focus on some technical challenges and how ideas from likelihood-free inference and machine learning can help overcome them. Timestamps 00:00Thomas Wiecki introduction 01:27Alex introduction 01:51Titi introduction 02:55Andy introduction 03:42Akili background 05:11EndeavorRx by Akili and PyMC's involvement 09:49Likelihood approximation networks in PyMC 10:15NeuroRacer 15:44Two important aspects of the Model 20:39Inference with model variants 21:05Inference from access to simulators 21:55Inference with models 22:56Training 24:06Previous toolbox: HDDM 24:59Properties inherited from Neural Networks 26:31Graphical representation of model in PyMC 29:42Code in PyMC 30:07Neural network (LAN, CPN) 31:17Proof of concept (Parameter Recovery) 31:42Proof of concept (Speed) 32:41Thomas question on speed 36:11Thomas on Before PyMC vs after PyMC 36:32Titi on before PyMC vs after PyMC 38:11Andy on production use case 39:00Thomas question on application 39:16Andy explains the use case and the application 40:28Titi on impact in applications 41:15Thomas on Knowledge transfer to Akili research team and collaboration 43:02Andy on working with PyMC team 44:55Thomas question to Alex on applying this method to other applications across industries 47:15Why does Akili care about these kinds of models ? 49:31PyMC's work and impact towards Akili's mission 51:04Audience Q/A (What other conditions can this be applied other than ADHD?) 52:03Audience Q/A (Is Data enough to conduct experiments ?) 56:32Closed form solution...

---

## 11. Bayesian Methods in Modern Marketing Analytics

**URL:** https://www.pymc-labs.com/blog-posts/2023-06-20-juan-marketing-analytics

**Description:** Discover the innovative application of Bayesian methods in the realm of modern marketing analytics. This article offers a fresh perspective on how these advanced techniques are reshaping the landscape of data-driven marketing strategies.

**Word Count:** 378

**File:** `011_2023-06-20-juan-marketing-analytics.txt`

**Summary:**

Bayesian Methods in Modern Marketing Analytics September 23, 2025 ByThomas Wiecki Introduction Bayesian methods have gained significant popularity in modern marketing analytics due to their ability to handle uncertainty, incorporate prior knowledge, and make accurate predictions. Unlike traditional statistical approaches, Bayesian methods provide a flexible framework that enables marketers to make data-driven decisions by combining observed data with prior beliefs or assumptions. Event Description In this webinar we discuss some of the most crucial topics in marketing analytics: media spend optimization through media mix models and experimentation, and customer lifetime value estimation. We approach these topics from a Bayesian perspective, as it gives us great tools to have better models and more actionable insights. We take this opportunity to describe our join with PyMC Labs in open-sourcing some of these tools in our brand-new pymc-marketing Python packagePyMC Marketing. Timestamps 00:00Welcome 02:03Webinar starts 02:32Webinar's objective 03:04Outline 04:05Applied Data Science 05:12Bayesian Methods 06:49Geo-Experimentation 08:27Time-Based Regression 10:26Regression model in PyMC 12:04Marketing measurement 13:34Media Transformations (Carryover (Adstock) & Saturation) 15:50Media Mix Model Target 16:24MMM Structure 16:53Media Contribution Estimation 17:13Budget Optimization 18:18PyMC-Marketing 19:25PyMC-Marketing- More MMM Flavours 20:00Customer Lifetime Value (CLV) 21:47Continuous Non-Contractractual CLV 22:57CLV Estimation Strategy 24:31BG/NBD Assumptions 27:14BG/NBD Parameters 27:50BG/NBD Probability of Alive 28:40Gamma-Gamma Model 29:12BG/NBD Hierarchical Models 31:14Causal Inference (Synthetic control) 32:10Causal Inference (Difference-in-Differences and Regression Discontinuity) 32:39Instrumental Variables 34:46Cohort Revenue-Retention Modelling 38:21Retention and Revenue component 41:02Cohort Revenue-Retention Model 42:34Revenue-Retention Predictions 43:11References 44:25Connect with PyMC Labs 44:50Marketing analytics strategy consultation 47:36PyMC Applied Workshop 48:58Q/A There are so many parameters in MMM which are not identifiable ... 53:00Q/A In the MMM how do you encode categorical control variables? 54:10Q/A How to deal with latent variables? 57:34Q/A If you observe the baseline uplift...How do you measure it in a Media mix model...? 59:15Q/A How does it solve the cold start problem? Resources pymc-marketing open source...

---

## 12. Building an in-house marketing analytics solution

**URL:** https://www.pymc-labs.com/blog-posts/2023-07-18-niall-In-house-marketing

**Description:** Get a fresh perspective on constructing an in-house marketing analytics solution. This article offers unique insights into the process, highlighting the benefits and challenges of such an endeavor.

**Word Count:** 0

**File:** `012_2023-07-18-niall-in-house-marketing.txt`

**Summary:**

No content available.

---

## 13. Developing Hierarchical Models for Sports Analytics

**URL:** https://www.pymc-labs.com/blog-posts/2023-09-15-Hierarchical-models-Chris-Fonnesbeck

**Description:** Grasp the intricacies of hierarchical models in the realm of sports analytics. This article presents a comprehensive analysis of these advanced techniques, highlighting their potential in transforming data-driven sports strategies.

**Word Count:** 0

**File:** `013_2023-09-15-hierarchical-models-chris-fonnesbeck.txt`

**Summary:**

No content available.

---

## 14. Latent Calendar: Modeling Weekly Behavior with Latent Components

**URL:** https://www.pymc-labs.com/blog-posts/2023-10-27-Latent-calendar-Will

**Description:**  We will delve into how Latent Dirichlet Allocation can be applied to discretized calendar events, allowing us to tap into the model's probabilistic origins and its connection to Bayesian principles, offering a wide array of potential applications and insights.

**Word Count:** 0

**File:** `014_2023-10-27-latent-calendar-will.txt`

**Summary:**

No content available.

---

## 15. Mastering Marketing Effectiveness: A Comprehensive Guide for Digital Marketers

**URL:** https://www.pymc-labs.com/blog-posts/2023-19-11-marketing-effectiveness

**Description:** In today's fast-paced digital marketing landscape, it's crucial to master measuring and understanding marketing strategies' effectiveness. This guide covers the importance of marketing effectiveness, explores various evaluation methods, and presents best practices for implementing an effective marketing measurement strategy.

**Word Count:** 0

**File:** `015_2023-19-11-marketing-effectiveness.txt`

**Summary:**

No content available.

---

## 16. AI-based Customer Research: Faster & Cheaper Surveys with Synthetic Consumers

**URL:** https://www.pymc-labs.com/blog-posts/AI-based-Customer-Research

**Word Count:** 831

**File:** `016_ai-based-customer-research.txt`

**Summary:**

AI-based Customer Research: Faster & Cheaper Surveys with Synthetic Consumers October 22, 2025 ByBenjamin F. Maier Consumer research costs corporations billions annually, yet it still struggles with panel bias, limited scale, and noisy results. What if synthetic consumers powered by large language models(LLMs) could replicate human survey responses with high accuracywhile providing richer qualitative feedback? That's exactly what PyMC Labs researchers just proved in anew preprintthat's changing how we think about AI-powered market research. The Problem with Asking AI for Numbers When companies first tried using LLMs assynthetic consumers, they hit a wall. Ask LLMs directly for a 1-5 rating about purchase intent given a product concept, and you get unrealistic distributions — too many "3s," hardly any extreme responses, and patterns that don't match real human behavior.The conventional wisdom?LLMs just aren't reliable survey takers. Our PyMC Labs teamshowed that'swrong.The problem wasn't the models, it was how we were asking them questions. The Breakthrough: Semantic Similarity Rating (SSR) Instead of forcing LLMs to pick a number, the research team developed a two-step approach: Step One:Let AI respond naturally in text (like humans actually think about purchase intent) Step Two:Map that response to a rating distribution on the 1-5 scale using semantic similarity, comparing the AI's statement to reference anchors for each point The results? Using 57 real consumer surveys from a leading consumer products company (9,300 human responses),the SSR method achieved: 90% correlation attainment with product ranking in human surveys More than 85% distributional similarity to actual survey results Realistic response patterns that mirror how humans actually rate products This isn't just incrementally better, it's the first approach that produces synthetic consumer data reliable enough to guide real product development decisions. What This Means for Business For Product Development Teams:You can now screen dozens of concepts with synthetic panels before...

---

## 17. Solving Real-World Business Problems with Bayesian Modeling

**URL:** https://www.pymc-labs.com/blog-posts/Thomas_PyData_London

**Description:**  A practical guide to solving business problems with Bayesian modeling

**Word Count:** 419

**File:** `017_thomas_pydata_london.txt`

**Summary:**

Solving Real-World Business Problems with Bayesian Modeling September 23, 2025 ByThomas Wiecki Introduction Among Bayesian early adopters, digital marketing is chief. While many industries are embracing Bayesian modeling as a tool to solve some of the most advanced data science problems, marketing is facing unique challenges for which this approach provides elegant solutions. Among these challenges are a decrease in quality data, driven by an increased demand for online privacy and the imminent "death of the cookie" which prohibits online tracking. In addition, as more companies are building internal data science teams, there is an increased demand for in-house solutions. In this talk Thomas explains how Bayesian modeling addresses these issues by: (i) Incorporating expert knowledge of the structure as well as about plausible parameter rangers. (ii) Connecting multiple different data sets to increase circumstantial evidence of latent user features. (iii) Principled quantification of uncertainty to increase robustness of model fits and interpretation of the results. Inspired by real-world problems we encountered at PyMC Labs, we will look at Media Mix Models for marketing attribution and Customer Lifetime Value models and various hybrids between them. About Speaker Dr. Thomas Wiecki is an author of PyMC, the leading platform for statistical data science. To help businesses solve some of their trickiest data science problems, he assembled a world class team of Bayesian modelers founded PyMC Labs -- the Bayesian consultancy. He did his PhD at Brown University studying cognitive neuroscience. GitHub:https://github.com/twiecki Twitter:https://twitter.com/twiecki Website:https://twiecki.io/ Timestamps 00:00Welcome! 0:05Speaker introduction and PyMC 4 release announcement 1:15PyMC Labs- The Bayesian consultancy 2:39Why is marketing so eager to adopt Bayesian solutions 3:49Case Study: Estimating Marketing effectiveness 6:00Estimating Customer Acquisition Cost (CAC) using linear regression 7:36Drawbacks of linear regression in estimating CAC 10:02Blackbox Machine learning and its drawbacks 11:27Bayesian modelling 11:52Advantages of Bayesian modelling 14:12How does Bayesian...

---

## 18. From Weeks to Minutes: Accelerate building your Bayesian Marketing Mix Model using Fivetran & PyMC-Marketing

**URL:** https://www.pymc-labs.com/blog-posts/accelerating-bayesian-mmm-fivetran-pymc-marketing

**Description:** Fivetran and PyMC-Marketing integrate to deliver a production-grade Bayesian MMM pipeline. Standardized dbt outputs flow directly into PyMC-Marketing loaders, enabling faster insights, defendable uncertainty estimates, and scalable budget optimization.

**Word Count:** 0

**File:** `018_accelerating-bayesian-mmm-fivetran-pymc-marketing.txt`

**Summary:**

No content available.

---

## 19. Unraveling Cause-and-Effect With AI: A Step Towards Automated Intelligent Causal Discovery

**URL:** https://www.pymc-labs.com/blog-posts/ai-for-causal-discovery

**Word Count:** 0

**File:** `019_ai-for-causal-discovery.txt`

**Summary:**

No content available.

---

## 20. Introducing the BETA Release of Our MMM Agent - Powered by PyMC-Marketing

**URL:** https://www.pymc-labs.com/blog-posts/ai-mmm-agent-beta

**Description:** We're thrilled to open up BETA access to the latest version of our Marketing Mix Modeling (MMM) Agent - a fully AI-driven assistant built on top of PyMC-Marketing that turns what used to be a multi-month modeling effort into an interactive, informative, and insightful workflow in hours.

**Word Count:** 0

**File:** `020_ai-mmm-agent-beta.txt`

**Summary:**

No content available.

---

## 21. Bayes is slow? Speeding up HelloFresh's Bayesian AB tests by 60x

**URL:** https://www.pymc-labs.com/blog-posts/bayes-is-slow-speeding-up-hellofreshs-bayesian-ab-tests-by-60x

**Description:** How to massively speed up inference for AB tests

**Word Count:** 0

**File:** `021_bayes-is-slow-speeding-up-hellofreshs-bayesian-ab-tests-by-60x.txt`

**Summary:**

No content available.

---

## 22. Application of Bayesian Computation in Finance

**URL:** https://www.pymc-labs.com/blog-posts/bayesian-computation-in-finance

**Description:** This blog post explores the transformative potential of Bayesian computation and PyMC in the field of finance. It highlights how Bayesian methods can enhance financial analysis by quantifying uncertainty, overcoming restrictive assumptions of traditional econometric models, and managing complex model structures with non-normal distributions. The post emphasizes the advantages of Bayesian statistics, such as its ability to provide a comprehensive and interpretable framework for decision-making under risk, and showcases practical applications using PyMC.

**Word Count:** 0

**File:** `022_bayesian-computation-in-finance.txt`

**Summary:**

No content available.

---

## 23. Bayesian inference at scale: Running A/B tests with millions of observations

**URL:** https://www.pymc-labs.com/blog-posts/bayesian-inference-at-scale-running-ab-tests-with-millions-of-observations

**Description:** Industry data scientists are increasingly making the shift over to using Bayesian methods. However, one often cited reason for avoiding this is because “Bayesian methods are slow.” 

**Word Count:** 0

**File:** `023_bayesian-inference-at-scale-running-ab-tests-with-millions-of-observations.txt`

**Summary:**

No content available.

---

## 24. Bayesian Baseball Monkeys

**URL:** https://www.pymc-labs.com/blog-posts/bayesian-marcel

**Description:** Using Bayesian methods to implement a MARCEL-style projection system for MLB ...

**Word Count:** 0

**File:** `024_bayesian-marcel.txt`

**Summary:**

No content available.

---

## 25. Bayesian Media Mix Modeling for Marketing Optimization

**URL:** https://www.pymc-labs.com/blog-posts/bayesian-media-mix-modeling-for-marketing-optimization

**Description:** Learn about Bayesian Media Mix Modeling

**Word Count:** 2070

**File:** `025_bayesian-media-mix-modeling-for-marketing-optimization.txt`

**Summary:**

Bayesian Media Mix Modeling for Marketing Optimization September 23, 2025 ByBenjamin Vincent A problem faced by many companies is how to allocate marketing budgets across different media channels. For example, how should funds be allocated across TV, radio, social media, direct mail, or daily deals? One approach might be to use heuristics, i.e. sensible rules of thumb, about what might be most appropriate for your company. For instance, a widely used approach is to simply set your marketing budget as a percentage of expected revenues. But this involves guesswork - something we want to avoid regardless of the size of the marketing budget involved. Fortunately, with Bayesian modeling, we can do better than this! So-calledMedia Mix Modeling(MMM) can estimate how effective each advertising channel is in gaining new customers. Once we have estimated each channel’s effectiveness we can optimize our budget allocation to maximize customer acquisition and sales. We at PyMC Labs had an opportunity to unleash our skills on Bayesian MMM’s in partnership withHelloFresh(check theircareers page). Our collaboration started after HelloFreshpresented their Bayesian MMMatPyMCCon 2020(make sure to check out theirMMM blog post). Out of the natural post-presentation discussion, we decided to work together to see how the PyMC Labs team could build upon the great work by HelloFresh’s data science team. In this blog post, we outline what you can do with MMM’s, introduce how they work, summarise some of the benefits they can provide, as well as covering some of the modeling challenges. In a follow-up blog post, we will discuss the specific model improvements we implemented. What is the Bayesian Media Mix Model? A Bayesian Media Mix Model (MMM) is a sophisticated statistical approach used to analyze and optimize the effectiveness of various marketing channels in driving customer acquisition and sales. This model applies Bayesian inference to...

---

## 26. Bayesian Vector Autoregression in PyMC

**URL:** https://www.pymc-labs.com/blog-posts/bayesian-vector-autoregression

**Description:** It's time to let go of your custom Gibbs sampler

**Word Count:** 1082

**File:** `026_bayesian-vector-autoregression.txt`

**Summary:**

Bayesian Vector Autoregression in PyMC September 23, 2025 ByRicardo Vieira A little bit of history In the seminal 1993paper"Bayes regression with autoregressive errors: A Gibbs sampling approach", Siddhartha Chib presented to economists the potential of Gibbs sampling in "realistic settings that were previously considered intractable from a Bayesian perspective". A cursory reading reveals a pattern that is quite characteristic of this early type of work. A time-series statistical model is first described, usually in a handful of equations —1 in this case—, followed by an intricate analysis of how the model joint-probability can be cut into conditionally independent blocks appropriate for Gibbs sampling. In that paper this amounts to no less than 9 equations! If one's model could not be easily cut into sample-able blocks,"auxiliary" variablescould always be added as topping, until such cut was found. As if this was not hard enough, early pioneers had to write their custom Gibbs sampling algorithms by hand, taking care to accommodate the existing computing limitations. Chib's paper makes mention of a powerful 33MHz machine. This process was somewhat alleviated by increasing compute power and by the advent of general purpose MCMC samplers likeBUGSandJAGS, and later more powerful Hamiltonian Monte Carlo samplers like those found inStanandPyMC. Surprisingly, many are still relying on custom Gibbs sampler algorithms tothis day. Perhaps begging their joint probabilities to factor nicely or chasing the auxiliary variables needed for their latest model ideas. Needless to say, with PyMC, we won't be doing any of this! Back to the present We will implement a Vector Autoregression (VAR) model, a powerful time series tool, to examine and forecast complex dynamic relationships between variables. VAR models are routinely used by most macroeconomic and policy-making institutions, and have been increasingly adopted in other areas. Some interesting applications include: To understand how VAR works,...

---

## 27. Can LLMs play The Price is Right?

**URL:** https://www.pymc-labs.com/blog-posts/can-llms-play

**Description:** Synthetic consumers—LLMs simulating human survey participants—are becoming a powerful tool for marketing and behavioral research. They promise faster iteration, lower costs, and broader flexibility than traditional panels. But for them to be useful, they need not only to sound realistic, but also to demonstrate some level of real-world reasoning.

A core question in this space: do LLMs “understand” prices?* That is, can they recognize how much everyday items cost, and make decisions based on that understanding?

**Word Count:** 0

**File:** `027_can-llms-play.txt`

**Summary:**

No content available.

---

## 28. Causal analysis with PyMC: Answering 'What If?' with the new do operator

**URL:** https://www.pymc-labs.com/blog-posts/causal-analysis-with-pymc-answering-what-if-with-the-new-do-operator

**Description:** Learn how to use Bayesian causal analysis with PyMC and the new do operator to answer 'What If?' questions.

**Word Count:** 0

**File:** `028_causal-analysis-with-pymc-answering-what-if-with-the-new-do-operator.txt`

**Summary:**

No content available.

---

## 29. What if? Causal inference through counterfactual reasoning in PyMC

**URL:** https://www.pymc-labs.com/blog-posts/causal-inference-in-pymc

**Description:** Unravel the mysteries of counterfactual reasoning in PyMC and Bayesian inference. This post illuminates how to predict the number of deaths before the onset of COVID-19 and how to forecast the number of deaths if COVID-19 never happened. A must-read for those interested in causal inference!

**Word Count:** 0

**File:** `029_causal-inference-in-pymc.txt`

**Summary:**

No content available.

---

## 30. Causal sales analytics: Are my sales incremental or cannibalistic?

**URL:** https://www.pymc-labs.com/blog-posts/causal-sales-analytics-are-my-sales-incremental-or-cannibalistic

**Description:** This post explores causal sales analytics, helping companies estimate whether sales from a new product are incremental or cannibalistic. The article discusses the complexities of such analysis and the need for bespoke causal models, ultimately enhancing decision-making for product portfolio management.

**Word Count:** 0

**File:** `030_causal-sales-analytics-are-my-sales-incremental-or-cannibalistic.txt`

**Summary:**

No content available.

---

## 31. Causal sales analytics: A deep-dive on discrete choice modeling

**URL:** https://www.pymc-labs.com/blog-posts/causal-sales-analytics-discrete-choice-modeling

**Description:** This post explores how PyMC Labs applied a discrete choice modeling framework to solve a challenging causal sales analytics problem for Colgate-Palmolive. The basic multinomial discrete choice model is more faithful to the underlying data generating process than the interrupted time series model we discussed in a previous blog post. It is also more flexible in that can take into account product attributes such as price and product availability (ACV) and estimates each attribute's impact on sales. However, it fails to capture complex patterns of cannibalization and incrementality. This limitation stems from the model's assumption that unobserved consumer preferences are independent, which leads to unrealistic proportional substitution among all products when a new product is introduced.

To overcome this, we developed a more advanced solution based on the nested logit discrete choice model. This model organizes products into hierarchical "nests" (e.g., by segment or brand) to account for correlations in unobserved consumer preferences within those nests. This allows for a more realistic understanding of how a new product's sales are generated, showing that sales of one product preferentially cannibalize from products in the same nest (i.e., similar products). This innovation of this approach represents a significant advancement in causal sales analytics, providing our client with a powerful tool to make better decisions about product launches and marketing.

**Word Count:** 0

**File:** `031_causal-sales-analytics-discrete-choice-modeling.txt`

**Summary:**

No content available.

---

## 32. CausalPy - causal inference for quasi-experiments

**URL:** https://www.pymc-labs.com/blog-posts/causalpy-a-new-package-for-bayesian-causal-inference-for-quasi-experiments

**Description:**  Unveil the power of CausalPy, a new open-source Python package that brings Bayesian causal inference to quasi-experiments. Discover how it navigates the challenges of non-randomized treatment allocation, offering a fresh perspective on causal claims in the absence of experimental randomization.

**Word Count:** 0

**File:** `032_causalpy-a-new-package-for-bayesian-causal-inference-for-quasi-experiments.txt`

**Summary:**

No content available.

---

## 33. Complete Guide to Cohort Revenue & Retention Analysis: Bayesian Modeling Approach

**URL:** https://www.pymc-labs.com/blog-posts/cohort-revenue-retention

**Description:** Explore how Bayesian methods can be applied to cohort-level customer lifetime value (CLV) models. This post focuses on combining retention and revenue components for improved forecasting and strategic insights in marketing.

**Word Count:** 0

**File:** `033_cohort-revenue-retention.txt`

**Summary:**

No content available.

---

## 34. Bayesian model to infer private equity returns from capital in and outflows

**URL:** https://www.pymc-labs.com/blog-posts/everysk

**Description:** Learn how PyMC Labs and Everysk collaborated to develop a Bayesian model that provides insights into private equity returns from capital in and outflows, and how this model differs from standard machine learning analyses.

**Word Count:** 0

**File:** `034_everysk.txt`

**Summary:**

No content available.

---

## 35. Announcing the Expert Access Program (EAP)

**URL:** https://www.pymc-labs.com/blog-posts/expert-access-program

**Description:** Teams face critical deadlines where models must be rigorous, but hiring consultants or adding headcount only solves problems temporarily. This is why we created the Expert Access Program — to give teams ongoing access to our experts, ensuring their models keep delivering value long after the initial build.

**Word Count:** 0

**File:** `035_expert-access-program.txt`

**Summary:**

No content available.

---

## 36. From Uncertainty to Insight: How Bayesian Data Science Can Transform Your Business

**URL:** https://www.pymc-labs.com/blog-posts/from-uncertainty-to-insight-how-bayesian-data-science-can-transform-your-business

**Word Count:** 0

**File:** `036_from-uncertainty-to-insight-how-bayesian-data-science-can-transform-your-business.txt`

**Summary:**

No content available.

---

## 37. Hierarchical Customer Lifetime Value Models

**URL:** https://www.pymc-labs.com/blog-posts/hierarchical_clv

**Description:** This post explores the application of hierarchical Bayesian models to Customer Lifetime Value (CLV) prediction, improving accuracy for customer cohorts, and addressing seasonality and data sparsity.

**Word Count:** 0

**File:** `037_hierarchical_clv.txt`

**Summary:**

No content available.

---

## 38. How Realistic Are Synthetic Consumers?

**URL:** https://www.pymc-labs.com/blog-posts/how-realistic-are-synthetic-consumers

**Description:** Evaluating LLMs on Political and Lifestyle Choices

**Word Count:** 0

**File:** `038_how-realistic-are-synthetic-consumers.txt`

**Summary:**

No content available.

---

## 39. AI Innovation Lab: An agentic platform for transforming product development

**URL:** https://www.pymc-labs.com/blog-posts/innovation-lab

**Description:** At PyMC Labs, we’re tackling a core problem in the CPG industry: product innovation is too slow, fragmented, and disconnected from real consumer needs.


**Word Count:** 1846

**File:** `039_innovation-lab.txt`

**Summary:**

AI Innovation Lab: An agentic platform for transforming product development August 20, 2025 ByNina Rismal Abstract At PyMC Labs, we’re tackling a core problem in the CPG industry: product innovation is too slow, fragmented, and disconnected from real consumer needs. TheAI Innovation Labis an end-to-end platform that uses AI-powered synthetic consumers and expert agent collaboration to streamline every stage of product development — from smarter concept briefs and design iteration to pricing simulation and market validation. Validated through custom metrics and real-world benchmarks, our U.S. panelreplicates up to 90% of consumer behavior patterns. And we’re just getting started — this is the foundation of a broader vision: where virtual consumer panel insights can be used to evaluate product characteristics, pricing and even marketing creatives and branding providing quantitative assessments that can be fed as priors in Bayesian models such as Media Mix Models. Reimagining Product Innovation with Synthetic Consumers and Agentic Frameworks Across the CPG industry, product innovation is falling behind. It’s too slow, too fragmented, and too costly — and too often, it’s disconnected from what real consumers actually want. In response, a growing number of startups and industry leaders have turned tosynthetic consumers: AI-generated personas built to mirror real-world behaviors, preferences, and decision patterns. The promise? Faster, cheaper feedback — without the delays and limitations of traditional market research. But at PyMC Labs, we asked a harder question:What would it take to not just accelerate product development, but fundamentally rethink it — combining agentic workflows, multimodal vision models, and validated insights grounded in our expertise in data-driven simulations? With one of our major clients in the CPG space, we have developed theAI Innovation Lab— a new way to turn ideas into market-ready products. Where Product Innovation Breaks Despite billions invested in research, design, and marketing, product innovation in...

---

## 40. How to use JAX ODEs and Neural Networks in PyMC

**URL:** https://www.pymc-labs.com/blog-posts/jax-functions-in-pymc-3-quick-examples

**Description:** Learn how to seamlessly integrate JAX-based ODE solvers and neural networks with PyMC for Bayesian modeling.

**Word Count:** 1410

**File:** `040_jax-functions-in-pymc-3-quick-examples.txt`

**Summary:**

How to use JAX ODEs and Neural Networks in PyMC September 23, 2025 ByRicardo Vieira and Adrian Seyboldt PyMC strength comes from its expressiveness. If you have a data-generating process and want to infer parameters of interest, all you need to do is write it down, choose some priors and let it sample. Sometimes this is easier said than done, especially the "write it down" part. With Python's rich ecosystem, it's often the case that you already have a generative function, but it's written in another framework, and you would like to use it in PyMC. Thanks to the highly composable nature of the PyMC backend, this is simple. Even simpler if that framework can also provide you gradients for free! In this blog post, we show how you can reuse code from another popular auto-diff framework, JAX, directly in PyMC. We will start with a dummy example by simply wrapping a pure function that already exists underpymc.math, and then show two real examples: reusing an ODE Solver from the Diffrax library and a CNN from the Flax library. This blog post won't explain in detail why we do things the way they are shown, but will only show you how to do it. If you want to have a better understanding, you should check the PyMC exampleHow to wrap a JAX function for use in PyMCand the relevant PyTensordocumentation ofOp. Without further ado, let's import some stuff. Wrapping a pure JAX function In this first example, we will wrap thejax.numpy.expfunction so you can use it in PyMC models. This is purely demonstrative, as you could usepymc.math.exp. We first create a function that encapsulates the operation (or series of operations) that we care about. We also save the jitted function into a variable. JAX'sjitfunction accepts a function and returns a...

---

## 41. My Journey Building PyMC Labs: Five Principles from Open Source that Boost Innovation at any Company

**URL:** https://www.pymc-labs.com/blog-posts/labs-principles

**Description:** 5 organizational principles that foster innovation at PyMC Labs

**Word Count:** 0

**File:** `041_labs-principles.txt`

**Summary:**

No content available.

---

## 42. Likelihood Approximations with Neural Networks in PyMC

**URL:** https://www.pymc-labs.com/blog-posts/likelihood-approximations-through-neural-networks

**Description:**  We use an example from cognitive modeling to show how differentiable likelihoods learned from simulators can be used with PyMC.

**Word Count:** 0

**File:** `042_likelihood-approximations-through-neural-networks.txt`

**Summary:**

No content available.

---

## 43. Marketing Mix Modeling : A Complete guide

**URL:** https://www.pymc-labs.com/blog-posts/marketing-mix-modeling-a-complete-guide

**Description:** This blog explains how Marketing Mix Modeling separates base and incremental sales, adds lag and saturation effects, and uses Bayesian methods to handle uncertainty. It also shows how these ideas are applied in practice, from early PyMC models at HelloFresh to more recent work with PyMC-Marketing at companies like Bolt.

**Word Count:** 0

**File:** `043_marketing-mix-modeling-a-complete-guide.txt`

**Summary:**

No content available.

---

## 44. Estimating a Candidate's Popularity over Time with Markov Processes

**URL:** https://www.pymc-labs.com/blog-posts/markov-process

**Description:**  Estimate French presidents' popularity across time with a Markov model

**Word Count:** 0

**File:** `044_markov-process.txt`

**Summary:**

No content available.

---

## 45. Unobserved Confounders, ROAS and Lift Tests in Media Mix Models

**URL:** https://www.pymc-labs.com/blog-posts/mmm_roas_lift

**Description:** Understanding the role of lift tests in calibrating Media Mix Models.When working with Media Mix Models (MMMs), calibration with lift tests is not just a technical step —it's essential for making these models reliable and actionable.

**Word Count:** 0

**File:** `045_mmm_roas_lift.txt`

**Summary:**

No content available.

---

## 46. Bayesian Media Mix Models: Modelling changes in marketing effectiveness over time

**URL:** https://www.pymc-labs.com/blog-posts/modelling-changes-marketing-effectiveness-over-time

**Description:**  we outlined what Bayesian Media Mix Models (MMM's) are, how they worked, and what insights they can provide.

**Word Count:** 0

**File:** `046_modelling-changes-marketing-effectiveness-over-time.txt`

**Summary:**

No content available.

---

## 47. Out of model predictions with PyMC

**URL:** https://www.pymc-labs.com/blog-posts/out-of-model-predictions-with-pymc

**Word Count:** 0

**File:** `047_out-of-model-predictions-with-pymc.txt`

**Summary:**

No content available.

---

## 48. Customer Lifetime Value in the non-contractual continuous case: The Bayesian Pareto NBD Model

**URL:** https://www.pymc-labs.com/blog-posts/pareto-nbd

**Description:** Exploring the Bayesian Pareto NBD model for predicting customer lifetime value and purchase behavior

**Word Count:** 0

**File:** `048_pareto-nbd.txt`

**Summary:**

No content available.

---

## 49. LLMs and Price Reasoning: Toward an Industry Benchmark

**URL:** https://www.pymc-labs.com/blog-posts/price-benchmark

**Description:** Novel LLM benchmark for evaluating the ability to estimate consumer product prices and reason strategically in an analogue of "The Price is Right" showcase game.

**Word Count:** 0

**File:** `049_price-benchmark.txt`

**Summary:**

No content available.

---

## 50. Probabilistic Time Series Analysis: Opportunities and Applications

**URL:** https://www.pymc-labs.com/blog-posts/probabilistic-forecasting

**Description:** Profound impact of Bayesian modelling on businesses decisions.

**Word Count:** 3179

**File:** `050_probabilistic-forecasting.txt`

**Summary:**

Probabilistic Time Series Analysis: Opportunities and Applications September 23, 2025 ByJuan Orduz Over the past few years, we've witnessed the profound impact of Bayesian modeling on businesses' decisions. In this post, we aim to delve into a specific area where Bayesian methods have demonstrated their transformative potential: probabilistic forecasting models. Forecasting is a critical component of business planning across industries—from retail inventory management to financial market analysis, from energy demand prediction to marketing budget allocation. Traditionally, businesses have relied on point forecasts that provide a single estimate of future values. While these approaches can work reasonably well under stable conditions, they often fail to capture the inherent uncertainty in real-world systems and can lead to suboptimal decisions when confronted with volatile or complex environments. Probabilistic forecasting addresses these limitations by generating complete probability distributions over possible future outcomes rather than single-point predictions. This paradigm shift provides decision-makers with a more comprehensive view of potential scenarios, enabling robust planning that accounts for risk and uncertainty. With recent advances in computational methods and Bayesian statistics, these sophisticated approaches have become increasingly accessible to practitioners. In this post, we'll explore how probabilistic forecasting models can provide a competitive advantage through their ability to incorporate domain expertise, handle data limitations, and model complex relationships. We'll demonstrate these capabilities through several case studies that showcase practical applications across different business contexts. Classical Time Series Forecasting Models In many business domains, such as logistics, retail, and marketing, we are interested in predicting the future values of one or more time series. Typical examples are KPIs like sales, conversions, orders, and retention. When businesses encounter forecasting challenges, they typically have two main approaches to consider: Use statistical methods to infer the trend, seasonality, and remainder components. Once we understand these components, we can use them to predict...

---

## 51. Running PyMC in the Browser with PyScript

**URL:** https://www.pymc-labs.com/blog-posts/pymc-in-browser

**Description:** Experience the power of PyMC in your browser with PyScript

**Word Count:** 784

**File:** `051_pymc-in-browser.txt`

**Summary:**

Running PyMC in the Browser with PyScript September 23, 2025 ByThomas Wiecki How is that possible? PyScript! PyScriptis a new (as of 2022) tool that allows you to execute Python directly in your browser. Previously, running code client-side was only possible with JavaScript. What's really exciting is that it's not just a small subset of Python, but everything. You can even import packages likeNumPy,Pandas, andMatplotlib. The way this works is viaPyodide, a port of the CPython runtime implemented in WebAssembly. If you want to learn more, watchPeter Wang'sPyCon 2022 Keynotewith many demos. Possible to run PyMC? Naturally, I was curious if it was possible to run PyMC through PyScript. On first thought this might seem impossible because PyMC compiles the model evaluation code to C or JAX (throughPyTensor). However,PyTensoralso has a Python mode which, while being much slower, is fully functional. Why? Before, you could have a PyMC model run on the server and then send the results back to the client (i.e. the browser). However, this has a few short-comings: It's challenging to set everything up to handle the interplay between client and server correctly, with many different technologies interacting in complex ways On top of the server<->client interplay, you have to pay special attention to scaling as many users might be running compute-extensive PyMC models in parallel Users might not be comfortable to send their data to your server If we can just run PyMC in the browser directly, all these problems go away. There is no interplay between client and server because everything runs on the client. There are no scaling issues because users use their own CPUs to fit their models. And finally, no data ever gets transmitted to the server, so it's completely safe and privacy preserving. The Process 1. Getting PyMC installed in the...

---

## 52. PyMC-Marketing: A Bayesian Approach to Marketing Data Science

**URL:** https://www.pymc-labs.com/blog-posts/pymc-marketing-a-bayesian-approach-to-marketing-data-science

**Description:** PyMC Labs is excited to announce the initial release of PyMC-Marketing

**Word Count:** 0

**File:** `052_pymc-marketing-a-bayesian-approach-to-marketing-data-science.txt`

**Summary:**

No content available.

---

## 53. PyMC-Marketing vs. Meridian: A Quantitative Comparison of Open Source MMM Libraries

**URL:** https://www.pymc-labs.com/blog-posts/pymc-marketing-vs-google-meridian

**Description:** This benchmark study directly compares PyMC-Marketing and Google’s Meridian on realistic synthetic datasets, from startup-scale to enterprise-level. Using aligned priors and identical configurations, it shows that PyMC-Marketing is consistently faster (2–20x), more accurate (lower error in channel contribution recovery, higher R², lower MAPE), and more scalable, thanks to its flexible sampling backends. Meridian remains leaner in storage size but suffers from slower performance, wider uncertainty, and convergence issues at scale. Overall, PyMC-Marketing emerges as the more robust, production-ready MMM library for data science teams.

**Word Count:** 0

**File:** `053_pymc-marketing-vs-google-meridian.txt`

**Summary:**

No content available.

---

## 54. MCMC for big datasets: faster sampling with JAX and the GPU

**URL:** https://www.pymc-labs.com/blog-posts/pymc-stan-benchmark

**Description:** Scaling PyMC using JAX to sample on the GPU

**Word Count:** 0

**File:** `054_pymc-stan-benchmark.txt`

**Summary:**

No content available.

---

## 55. Improving the Speed and Accuracy of Bayesian Media Mix Models

**URL:** https://www.pymc-labs.com/blog-posts/reducing-customer-acquisition-costs-how-we-helped-optimizing-hellofreshs-marketing-budget

**Description:** Using Bayesian MMM's to reduce customer acquisition costs

**Word Count:** 940

**File:** `055_reducing-customer-acquisition-costs-how-we-helped-optimizing-hellofreshs-marketing-budget.txt`

**Summary:**

Improving the Speed and Accuracy of Bayesian Media Mix Models September 23, 2025 ByBenjamin Vincent The data scientists atHelloFreshhave a big job on their hands. As part of a rapidly growing company with a worldwide reach, they influence the allocation of marketing dollars every year. One of their tasks is to maximize new customer acquisitions from data-driven insights. As part of their approach, the data scientists built a BayesianMedia Mix Model(seethis videofor more details). If you want a refresher of the power of Bayesian Media Mix Models, check out ourprevious blog post. But in short, MMM’s help us understand the characteristics and effectiveness of different marketing channels like TV, radio, podcasts, social media, daily deals, and more, based on how much we spent on each channel over time and how many new users we acquired. Given the scale of HelloFresh’s operations, even minor improvements in the insights gained by such models can have significant effects on new customer acquisitions. Recently HelloFresh’s data scientists challenged us to do precisely this - could we (PyMC Labs) help them improve theiralready sophisticated Bayesian MMM? What we delivered to HelloFresh More accurate and precise model predictions Thanks toPyMC3, we can build a model, feed in data, and press the Inference Button™. However, making high profile decisions requires due diligence! One crucial way of doing this is inspectingposterior predictive checks, which are plots comparing the model’s predicted customer acquisitions to the actual data. The closer the match between predictions and actuals, the greater confidence we can have in the model. By inspecting PPC plots, we could identify two key improvements to the model: We changed the outcome variable to be thelogarithmof the number of new customers rather than the actualrawnumber. This can be useful in situations where there might be signal-dependent noise (i.e. more measurement...

---

## 56. Introducing PyMC Labs

**URL:** https://www.pymc-labs.com/blog-posts/saving-the-world

**Description:** Discover how PyMC Labs is helping organizations solve complex problems using Bayesian modeling.

**Word Count:** 1089

**File:** `056_saving-the-world.txt`

**Summary:**

Introducing PyMC Labs September 23, 2025 ByThomas Wiecki After I left Quantopian in 2020, something interesting happened: various companies contacted me inquiring about consulting to help them with their PyMC3 models. Usually, I don't hear how people are usingPyMC3-- they mostly show up onGitHuborDiscoursewhen something isn't working right. So, hearing about all these really cool projects was quite exciting. However, I couldn't possibly take all of these projects on by myself. Thus, it was time to assemble a team of the most badass Bayesian modelers the world had ever seen -- the Bayesian Avengers, if you will. Fortunately, I did not have to venture far, as PyMC3 had already attracted exactly these types of people. This brings me to the Big Announcement: For the last few months, we have quietly been buildingPyMC Labs, a Bayesian modeling consultancy.We have an amazing teamconsisting of three neuroscience PhDs, mathematicians, social scientists, a SpaceX rocket scientist, and the host of the famous‘Learning Bayesian Statistics’ podcast. All of us are united in our mission: Saving the world with Bayesian modeling Does this sound a bit grandiose? Probably. Is this true? I firmly believe it is. There are so many important problems the world faces today -- from climate change to COVID19, from education to poverty -- and Bayesian modeling can play a critical role in solving these problems. Let me explain why. It is already doing it I would not have imagined it when I started contributing to PyMC, but the science PyMC3 has directly enabled ranges fromclimate scienceand biology to astronomy and zoology, and everything in between. For instance, it was used to predict the spread of COVID19 in a recentScience paper, as well astrack the reproduction factor in real-time. In both cases, the benefit of PyMC3 was its ease-of-use and the ability to...

---

## 57. Simulating data with PyMC

**URL:** https://www.pymc-labs.com/blog-posts/simulating-data-with-pymc

**Description:** Explore how PyMC can be used for efficient and powerful data simulation.

**Word Count:** 1033

**File:** `057_simulating-data-with-pymc.txt`

**Summary:**

Simulating data with PyMC September 23, 2025 ByRicardo Vieira and Tomás Capretto Image fromWikipedia PyMCprovids a great API for defining statistical models. When paired with its sampling algorithms, it becomes the ideal tool for conducting reliable and robust Bayesian inference. Still, Bayesian inference is far from its only use case. PyMC models specify a highly structured data-generating process that can be very useful on its own. Applications include simulation for optimization routines, risk analysis, and research design, among many others. PyMC comes with many user-friendly builtin distributions and meta-distributions which are cumbersome to write from scratch with NumPy or SciPy routines. These include Mixtures, Timeseries, Multivariate parametrizations, Censored and Truncated distributions, and pretty much anything you would would ever need when doing data simulation. In this blog post we will give you a flavor for some of these, and show how we use them as part of a data modelling workflow! Taking draws from simple distributions SciPy has a lot of distributions, but they are often difficult to work with, due to their focus on loc-scale parametrizations. PyMC tends to pick more intuitive parametrizations (and often offers multiple options). For instance, in PyMC you can define aGammadistribution using the shape/rate parametrization (which we call alpha and beta), and then take draws with thedrawfunction. Or, perhaps more intuitively, using the mean/standard deviation parametrization (called mu and sigma). PyMC takes care of converting between equivalent parametrizations for the user. All PyMC distributions are vectorized Not all SciPy distributions allow NumPy-like broadcasting for their parameters. PyMC distributions always do! Ah well... Meta-Distributions Neither NumPy nor SciPy offer a pre-built truncated LogNormal distribution (last time I checked). They do offer a Truncated Normal, and you could exponentiate those to obtain Truncated LogNormal draws. But what if you wanted to sample some other truncated distribution?...

---

## 58. Modeling spatial data with Gaussian processes in PyMC

**URL:** https://www.pymc-labs.com/blog-posts/spatial-gaussian-process-01

**Description:** We build a Gaussian process model on a geospatial dataset with the goal of predicting expected concentrations of a radioactive gas in households depending on the county the houses belong to.

**Word Count:** 1802

**File:** `058_spatial-gaussian-process-01.txt`

**Summary:**

Modeling spatial data with Gaussian processes in PyMC September 23, 2025 ByThomas Wiecki Beyond naive hierarchical models So many times I've found myself having to work with geospatial data. It's everywhere: from advertisement, to product inventories, to electoral polls. While I was learning Bayesian modeling, I used to think about geographical information as some categorical value that grouped some observations together. The nice thing about this approach is that observations coming from the exact same geographical area will share a common feature, and this feature will be used (somehow) to explain the similarities between both observations. The bad thing about this approach is that observations from neighboring geographical areas are assumed to have absolutely nothing in common. Sounds weird, right? Usually we would picture some kind of continuous latent geographical feature that makes observations taken from nearby places be similar to each other. Surely there must be a better way of modeling geospatial data! Completely independently from me modeling geospatial data, I learned how to work with Gaussian processes (GPs). GPs provide a very nice and flexible way of setting a prior that essentially says:"nearby observations should be similar to each other, and as the observations go further away, they become uncorrelated". This really clicked with what I wanted to do with geospatial data! The only problem was that there weren't many sources targeting general audiences that explained how to use GPs on geospatial data. That's why I wanted to put together a small example that showcases how you can use GPs with geospatial data using PyMC. Our dataset We will be revisiting a classic: the radon dataset, fromGelman and Hill 2006(if you haven't read thePyMC case studyyet, you really should go ahead and do that now, it's an excellent resource!). Just to give you a quick refresher, Gelman and...

---

## 59. Synthetic Consumers: The Promise, The Reality, and The Future

**URL:** https://www.pymc-labs.com/blog-posts/synthetic-consumers

**Description:** 📢 Announcing Our First White Paper: "Synthetic Consumers: The Promise, The Reality, and The Future"

**Word Count:** 308

**File:** `059_synthetic-consumers.txt`

**Summary:**

Synthetic Consumers: The Promise, The Reality, and The Future September 23, 2025 ByNina Rismal,Luca Fiaschi Synthetic consumers – AI-generated personas designed to simulate human consumer behavior – are rapidly transforming market research by deliveringfaster,cost-effective, and highly scalable insightscompared to traditional methods. By 2027,synthetic responses are expected to constitute over half of all marketresearch data,highlighting the urgency for businesses to understand and adopt this technology strategically. This white paper equips technical business leaders, consumer insights experts, anddata scientists with clear and actionable knowledge about this technology. Key Insights Defining Synthetic Consumers: We clearly define synthetic consumers anddistinguish them from related concepts like digital twins, synthetic respondents,and human simulacra. Defining Synthetic Consumers: We clearly define synthetic consumers anddistinguish them from related concepts like digital twins, synthetic respondents,and human simulacra. Real-World Use Cases: We highlight practical examples of synthetic consumersapplications currently used by both major companies and startups for producttesting, innovation, data augmentation, and consumer insights. Real-World Use Cases: We highlight practical examples of synthetic consumersapplications currently used by both major companies and startups for producttesting, innovation, data augmentation, and consumer insights. Accuracy and Validation: We analyze methods for evaluating synthetic consumeraccuracy, summarizing recent research that increasingly shows confidence in thealignment between synthetic and human responses across multiple domains. Accuracy and Validation: We analyze methods for evaluating synthetic consumeraccuracy, summarizing recent research that increasingly shows confidence in thealignment between synthetic and human responses across multiple domains. PyMC Labs offers unique expertise by creating customized solutions that combineadvanced Generative AI with science-based benchmarking. Our rigorous andtransparent methods allow clients to confidently use synthetic consumer insights forclear business value. In this paper, we aim to provide a balanced view on synthetic consumers,highlighting their transformative potential while recognizing their current limitations. ###📖 Read the Full Paper Here 🔗Download the white paper now Join us in redefining...

---

## 60. Can Synthetic Consumers Answer Open-Ended Questions?

**URL:** https://www.pymc-labs.com/blog-posts/synthetic-consumers-open-ended-responses

**Description:** Evaluating LLMs on generating open-ended text responses.Synthetic consumers are revolutionizing market research by making it faster, less expensive, and more flexible.

**Word Count:** 1055

**File:** `060_synthetic-consumers-open-ended-responses.txt`

**Summary:**

Can Synthetic Consumers Answer Open-Ended Questions? September 23, 2025 ByAllen Downey Evaluating LLMs on generating open-ended text responses Synthetic consumers are revolutionizing market researchby making it faster, less expensive, and more flexible. One especially valuable capability is their ability to generate responses to open-ended questions. This enhances the depth and richness of insights typically associated with qualitative research. Of course, synthetic consumers are only useful if their responses are similar to those of real people. To see whether they are, we are conducting a series of experiments to test synthetic consumers using public datasets and representative survey questions. Inthis previous post, we used data from the General Social Survey to see how well synthetic panels replicate real responses to a categorical question. Our insight? Although some models did better than others, the best responses were about as good as the results from a machine learning algorithm (random forest) trained with data from 3000 respondents. Now we’re ready for a more challenging test, generating open-ended text. Identifying the Most Important Problems We use data from the American National Election Studies (ANES)2020 Time Series Study, which includes several open-ended questions. The one we’ll look at is “What do you think are the most important problems facing this country?” We chose this question because we expect the responses to be moderately predictable based on demographic information about the respondents. To see whether the responses we get from synthetic consumers are consistent with real people, we randomly selected a test set of 100 respondents. For each respondent, we collected demographic information including age, gender, race, education, income, occupation, and religious affiliation, as well as responses to the following question about political alignment, “Where would you place yourself on this scale?” from extremely liberal--point 1--to extremely conservative--point 7. To test synthetic consumers, we composed a...

---

## 61. The AI MMM Agent, An AI-Powered Shortcut to Bayesian Marketing Mix Insights

**URL:** https://www.pymc-labs.com/blog-posts/the-ai-mmm-agent

**Description:** AI revolutionizes marketing analytics by dramatically accelerating the traditional marketing mix modeling (MMM) process. This AI agent automates PyMC-Marketing workflows, delivering MMM results in hours instead of months.

**Word Count:** 1638

**File:** `061_the-ai-mmm-agent.txt`

**Summary:**

The AI MMM Agent, An AI-Powered Shortcut to Bayesian Marketing Mix Insights September 23, 2025 ByLuca Fiaschi Abstract: What if you could transform raw spend data into boardroom strategy in just one day? For CMOs, waiting months for marketing mix modeling (MMM) results is no longer an option. AI is revolutionizing the marketing analytics industry by dramatically accelerating the traditional modeling and insight workflow. In this post, we showcase an AI agent that automates PyMC-Marketing workflows—delivering MMM results in hours instead of months. Discover how it converts raw spend data into boardroom-ready strategy while balancing technical rigor with executive clarity. The Traditional MMM Bottleneck: Why Teams Get Stuck Building a Bayesian marketing mix model today often feels like assembling a plane mid-flight. The process is fraught with obstacles that slow progress at every turn: Data Prep Chaos:Teams frequently spend weeks merging siloed data—from sales and ads to promotions—while wrestling with discrepancies. Questions like, “Are these TikTok spend numbers from Q2 accurate?” or “Why does the CRM data conflict with GA4?” are common. These gaps and inconsistencies require experienced analysts to identify issues and implement painstaking manual fixes. Model-Building Guesswork:Once the data is ready, the challenge shifts to model configuration. Data scientists grapple with decisions such as whether the adstock decay should be 30 or 45 days, or if saturation is best modeled using a Hill curve or an exponential function. This trial-and-error approach can involve testing over ten different configurations while battling issues like multicollinearity and the risk of overfitting. Validation Black Holes:Even with a model in place, validation can become a black hole. When the MCMC sampling won’t converge, experts are left questioning whether the problem lies with the priors or the underlying spend data. Debugging often consumes more time than building the model itself. Stale Insights Syndrome:By the...

---

## 62. The Quickest Migration Guide Ever from PyMC3 to PyMC v4.0

**URL:** https://www.pymc-labs.com/blog-posts/the-quickest-migration-guide-ever-from-pymc3-to-pymc-v40

**Description:** Discover how few changes are needed to upgrade to PyMC v4.0!

**Word Count:** 550

**File:** `062_the-quickest-migration-guide-ever-from-pymc3-to-pymc-v40.txt`

**Summary:**

The Quickest Migration Guide Ever from PyMC3 to PyMC v4.0 September 23, 2025 ByEric J. Ma PyMC v4.0is out in beta! PyMC Labs is thrilled to have worked with the PyMC development team to get this release out the door. Usually, a new version implies code changes. In this short post, we’d like to highlight how to migrate your code from PyMC3 to PyMC v4.0. The tl;dr? While there’s a lot of really cool improvements we’ve made underneath the hood (stay tuned for a full post on this), the number of things you’ll need to change areminimal! Installation PyMC v4.0 is now available viapipandconda. To install bypip: (The--preflag is necessary to install the pre-release before we release the a production-ready version.) To install byconda: Imports The biggest change you’ll see is probably this one. You probably imported PyMC3 as follows: With PyMC v4.0, you’ll do the following import instead: Sampling In PyMC3, we used to return aMultiTraceobject. In PyMC v4.0, we instead return an ArviZInferenceDataobject instead: Underneath the hood, theInferenceDataobject is a richer data structure than the MultiTrace object, and is essentially a wrapper around xarray. Xarray provides the ability to do much saner indexing and labelling of coordinates. You can think of xarray as “pandas for n-dimensional arrays”. You can read more about theInferenceDataobject onthe official ArviZ docs. In addition to that theInferenceDataobject supports storing prior predictive and posterior predictive samples that you can use to sanity-check your models. If you do this often, stay tuned for API updates to PyMC v4.0:we are discussingmaking prior and posterior predictive samples a standard part ofpm.sample()itself! ArviZ In the past, you may have used PyMC3’s built-in visualization capabilities: Since PyMC3, we’ve started delegating these visualization capabilities to ArviZ, and as of PyMC v4.0, it’s considered idiomatic to just use ArviZ instead. ArviZ...

---

## 63. Write Me a PyMC Model

**URL:** https://www.pymc-labs.com/blog-posts/write-me-a-pymc-model

**Description:** ModelCraft is an AI agent that writes, checks, and refines PyMC models — turning natural language prompts into validated Bayesian code. Built during a PyMC Labs hackathon, it combines LLMs, LangGraph, and a secure compiler to eliminate hallucinated functions and broken models, making Bayesian modeling faster and easier for all.

**Word Count:** 863

**File:** `063_write-me-a-pymc-model.txt`

**Summary:**

Write Me a PyMC Model September 23, 2025 ByBernard (Ben) Mares,Allen Downey,Alexander Fengler Hacking an agent to generate hallucination-free Bayesian models Writing a PyMC model is not easy. It requires familiarity with both statistical distributions and Python libraries. And if at first you don’t succeed, debugging can be a challenge. Large language models like GPT-4 are surprisingly capable at generating probabilistic models. You can give them a few sentences describing a Bayesian problem, and they will often respond with runnable PyMC code. But, as anyone who’s tried this knows, the quality of the results varies – and demonstrates a variety of failure modes. Sometimes the code is out of date — usingpymc3imports or old syntax. Sometimes it violates best practices, and occasionally the model won’t even compile, thanks to hallucinated functions or subtle shape mismatches. We wanted to fix that. So, during our internalProbabilistic AI hackathon, we builtModelCraft— an LLM-powered modelling agent that doesn't just generate PyMC code, but alsochecks its own work. Before it returns anything to the user, it runs the model through a remote compiler, catches errors, and rewrites the model if necessary. The goal: make it easier for beginners and experts alike to go from modelling ideas to validated PyMC code — all through natural language. How it works ModelCraft acts as a simple conversational agent that helps users write and validate PyMC models through natural language. You describe the model you want — the context, priors, data, whatever — and the agent responds with a complete PyMC model that’s been checked for correctness, at least in the sense that it compiles. Behind the scenes ModelCraft uses an LLM and LangGraph to generate candidate models and evaluate them using a secure code sandbox. This isn’t just code generation — the agent actually compiles each model before...

---

