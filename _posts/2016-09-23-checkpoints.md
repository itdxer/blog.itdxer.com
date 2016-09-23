---
title: "Saving partial Machine Learning results with Checkpoints"
date: 2016-09-23
---

In this post I would like to talk about a problem which I often encounter while I build Machine Learning models.

It's really can be annoying when overall training process takes too long and it's hard to experiment and improve model's accuracy when you need to execute the main script over and over again. Even small changes in the script lead to execution of all steps starting from data cleaning and ending with model validation during the cross validation. This process is just inefficient. That's why I used to spend some time preparing a good environment to store cleaned dataset in temporary CSV file and used it for experiments with different models. I've seen that some other people do the same thing when they try to make their experiments faster. In my opinion, if some problems occur often and interrupt the workflow they should be optimized.

I've tried different ways to solve this problem and finally I came up with something that I found really helpful. I called this method Checkpoints. The idea is simple, you separate all training processes into a few steps that should be triggered one after another in the specified order. When you run it for the first time, script saves partial results after each step. When you run the script for the second time you can specify which steps you don't want to run again. For these steps, script will restore saved results and use them for the next steps. Let's look at a simple example.

{% highlight python %}
from some_utils import *

dataset = read_data_from_csv()
dataset = clean_data(dataset)
dataset = add_new_features(dataset)

model = LogisticRegression()
model.fit(dataset)
{% endhighlight %}

Let's say we want to separate the code into three steps:

1. Clean the data
2. Extract some new features from the dataset
3. Train the model (I ignored cross validation and model evaluation steps for simplicity)

Let's split the code into different steps.

{% highlight python %}
from dslib.checkpoint import Checkpoint
from some_utils import *

class ModelTraining(Checkpoint):
    def step_1(self, outputs):
        dataset = read_data_from_csv()
        cleaned_dataset = clean_data(dataset)
        return cleaned_dataset

    def step_2(self, outputs):
        dataset = outputs['step_1']
        dataset = add_new_features(dataset)
        return dataset

    def step_3(self, outputs):
        dataset = outputs['step_2']
        model = LogisticRegression()
        model.fit(dataset)
        return model

if __name__ == '__main__':
    checkpoints = ModelTraining(
        name='model-training',
        checkpoint_folder='/path/to/checkpoint/folder',
        version=1,
    )
    checkpoints.run(start_from=2)
{% endhighlight %}

As you can see now everything is separated into three steps (``step_1``, ``step_2`` and ``step_3``) that defined as methods of the ``Checkpoint`` class. Each method accepts one parameter that stores outputs from the previous steps. Also each method returns something that we want to save as a partial progress. When we define all methods we can run them. To do that we need to initialize the ``ModelTraining`` instance which accepts three arguments. The first one is a ``name`` argument which will be used as a prefix for checkpoint file name. The second one just a path to the folder that stores partial results. And the third one is a version. Each unique version has its own checkpoints.

Last line in the code triggers method ``run`` with argument ``start_from`` that equal to 2. This method runs steps one by one in numerical order. The argument ``start_from=2`` means that we want to get result before the second step from the stored file and run all other (including second one) as usual. In case if we don't have checkpoint related to the first step then it will be forced to run step one.

After the training it's useful to check the residuals. I usually use iPython notebooks for this purpose. In the notebook you can read all stored instances and use them to explore your model.

{% highlight python %}
from main_script import ModelTraining

checkpoints = ModelTraining(
    name='model-training',
    checkpoint_folder='/path/to/checkpoint/folder',
    version=1,
)
outputs = checkpoints.load_outputs()
{% endhighlight %}

I'm used to making different versions after some important changes. In that way it helps me to reproduce old results from notebooks.

All files are stored in the pickle format and you can save everything that can be serialized with the [Pickle](https://docs.python.org/3.5/library/pickle.html) library. You do not necessary need to use checkpoints to read them. You can just load the stored results with Pickle. Also pickle saves and loads pandas data frames faster that makes overall process more efficient.

I put ``Checkpoint`` class on [Github](https://github.com/itdxer/dslib). In case if you find bug related to the code you can create issue [here](https://github.com/itdxer/dslib/issues).

I hope that this solution will help somebody to solve the same problem.
