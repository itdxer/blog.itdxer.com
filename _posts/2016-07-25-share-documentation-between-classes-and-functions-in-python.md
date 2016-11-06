---
title: "Share Documentation Between Classes and Functions in Python"
date: 2016-07-25
layout: post
description: ""
tags: [python, software development]
comments: true
share: false
---

For my [open-source project](https://github.com/itdxer/neupy) I write a lot of documentation that I then convert into HTML pages. When project grows it's difficult to support such amount of documentation. Mostly because there are a lot of copy and paste that occur in the code. To resolve this problem I came up with a solution that I call **Shared Docs**. Before I explain it to you I would like to show you an example of some common problem that happens in the projects that use Python's documentation.

## Problem

Let's assume that we need to make a small library. This library is supposed to have a bunch of classes that define people with different professions. Some attributes like person's name are the same for all classes and some are not. The problem is simple, right? Anyone who knows [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming) can make this library easily.

For this problem we need to have a class that will be a base class for all others. We can create a class ``Person`` which have attributes typical for any person with any profession.

{% highlight python %}
class Person(object):
    """
    Person class.

    Parameters
    ----------
    fullname : str
        Full name.
    height : float
        Height in meters (m).
    weight : float
        Weight in kilograms (kg).
    """
    def __init__(self, fullname, height, weight):
        self.fullname = fullname
        self.height = height
        self.weight = weight
{% endhighlight %}

Pretty simple, right? We have the class that identifies a person. We even have documentation that describes person's properties which is very useful, especially for weight and height parameters, because it's not really clear what units should we use to define these parameters.

{% highlight python %}
>>> john = Person(fullname="John Smith", height=1.8, weight=90)
{% endhighlight %}

But if anyone checks the documentation the one will find all necessary information there. Let's have a look.

    >>> help(john)
    Help on Person in module __main__ object:

    class Person(builtins.object)
     |  Person class.
     |
     |  Parameters
     |  ----------
     |  fullname : str
     |      Full name.
     |  height : float
     |      Height in meters (m).
     |  weight : float
     |      Weight in kilograms (kg).

Yep, now it's clear. Everything is defined in metric units.

So far everything works great. We have a class and documentation for it, so anyone can understand it.

Now we need to make a new class that depends on the ``Person`` class. Let it be a Doctor. Doctor is a person, so parameters should be the same as for the ``Person`` class.

{% highlight python %}
class Doctor(Person):
    """
    Doctor class.

    Parameters
    ----------
    fullname : str
        Full name.
    height : float
        Height in meters (m).
    weight : float
        Weight in kilograms (kg).
    specialty : list of str
        Doctor's speciality.
    """
    def __init__(self, specialty, *args, **kwargs):
        super(Doctor, self).__init__(*args, **kwargs)
        self.specialty = specialty
{% endhighlight %}

The new class has all the same properties and the old one. In addition, I've added a property that defines doctor's specialty. The other properties remain the same without changes.

For a while everything seems to work great until someone decided that we need to change height and weight properties to the imperial units. Now we need to find all places where we defined these stuff as metric units and change them to imperial units. And it feels very annoying when you work in a big project.

It becomes even worse when your project has deadlines. Things become tough when deadline is approaching. No one wants to waste time on documentation updates, because it takes a lot of time and energy to do that. Adding new features and bug fixing are more important.

Simple and obvious solution is not to write documentation at all, but in some cases it's important. Especially when the whole team is divided into small groups and each group is responsible for a separate component of the project. In that case other groups might be not familiar well enough with some of the components and documentation that explains parts of the unfamiliar components becomes very useful.

One way to approach these problems is Shared Docs.

## Solution: Shared Docs

Python's documentation is just string and it doesn't have standardized syntax which means that we need to choose one. Otherwise it will be difficult to identify variables in the documentation. I like [NumPy's documentation style](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt) and I use it for all my projects. My Shared Docs implementation works only with NumPy documentation style.

### Classes

Let's rewrite previous example using Shared Docs.

{% highlight python %}
from neupy.core.docs import SharedDocs

class Person(SharedDocs):
    """
    Person class.

    Parameters
    ----------
    fullname : str
        Full name.
    height : float
        Height in meters (m).
    weight : float
        Weight in kilograms (kg).
    """
    def __init__(self, fullname, height, weight):
        self.fullname = fullname
        self.height = height
        self.weight = weight
{% endhighlight %}

The Person class is exactly the same as we have seen before, but now it inherits from the ``SharedDocs`` class. So we need to rewrite the ``Doctor`` class.

{% highlight python %}
class Doctor(Person):
    """
    Doctor class.

    Parameters
    ----------
    {Person.fullname}
    {Person.height}
    {Person.weight}
    specialty : list of str
        Doctor's speciality.
    """
    def __init__(self, specialty, *args, **kwargs):
        super(Doctor, self).__init__(*args, **kwargs)
        self.specialty = specialty
{% endhighlight %}

This is a place where we start to take an advantage of this approach. As you can see we no longer need to copy and paste the documentation from the parent class. We just reuse it applying simple [Python format syntax](https://docs.python.org/3/library/string.html#format-string-syntax). In this way it's also seems clear which methods we reuse and from what class we inherit them.

The other way of doing it is just simply inherit all parameters at once.

{% highlight python %}
class Doctor(Person):
    """
    Doctor class.

    Parameters
    ----------
    {Person.Parameters}
    specialty : list of str
        Doctor's speciality.
    """
    def __init__(self, specialty, *args, **kwargs):
        super(Doctor, self).__init__(*args, **kwargs)
        self.specialty = specialty
{% endhighlight %}

As you can see I just replaced parameters with one variable that contains all parameters from the ``Person`` class. The main point of this variable is to make dynamic updates for the documentation. For instance, if we add a new parameter for the ``Person`` class that defines person's age, we just need to describe it in the ``Person`` class and the ``Doctor`` class will get it automatically, because it inherits all parameters from the parent class. The main disadvantage is that it's hard to understand which properties ``Doctor`` has when we read documentation from the code. But in other circumstances you will see properly formatted documentation.

    >>> help(Doctor)
    class Doctor(Person)
     |  Doctor class.
     |  
     |  Parameters
     |  ----------
     |  fullname : str
     |      Full name.
     |  height : float
     |      Height in meters (m).
     |  weight : float
     |      Weight in kilograms (kg).
     |  specialty : list of str
     |      Doctor's speciality.

So far I have only shown instances where we defined parameters, but Shared Docs can parse other variables like [Methods and Attributes](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt#class-docstring). Some sections like Warns or Returns are possible to be re-used as well, but in that case you can use entire section and it wouldn't be possible to divide it into smaller pieces.

### Functions

Sometimes it's also useful to inherit documentation for the functions that have similar behavior. Let's check another example. Just pretend that we try to build HTML page using python functions and we want to use it like this.

{% highlight python %}
html_page = div(
    div(
        h1('Title #1'),
        div('Some text')
    ),
    div(
        h1('Title #2'),
        div('Another text')
    )
)
{% endhighlight %}

Classes are redundant in this situation, so we can use functions. We can make a simple function that creates any opening and closing tags.

{% highlight python %}
def tag(name, *inner_tags):
    """
    Create HTML tag.

    Parameters
    ----------
    name : str
        HTML tag name.
    *inner_tags
        Children tags.
    """
    return "<{tag_name}>{}</{tag_name}>".format(
        ''.join(inner_tags),
        tag_name=name
    )
{% endhighlight %}

This function creates any tag we want. We can create a span tag.

{% highlight python %}
>>> tag('span', 'Hello world')
<span>Hello world</span>
{% endhighlight %}

It works, but it's not a Pythonic way to do it. To make it look better we can define a few functions that will create only a specific tag like ``h1`` or ``div``.

The HTML tag will have pretty much the same input parameters, which means that we need to make the same parameters description in the documentation. Shared Docs can be useful in this situation too. To get the same ability to inherit documentation from other functions we may use ``shared_docs`` decorator.

{% highlight python %}
from neupy.core.docs import shared_docs

@shared_docs(tag)
def h1(*inner_tags):
    """
    Create level one header tag.

    Parameters
    ----------
    {tag.inner_tags}
    """
    return tag('h1', *inner_tags)

@shared_docs(tag)
def div(*inner_tags):
    """
    Create div tag.

    Parameters
    ----------
    {tag.inner_tags}
    """
    return tag('div', *inner_tags)
{% endhighlight %}

And if we check documentation for the one of the classes we will see that everything is formatted properly.

    >>> help(div)
    Help on function div in module __main__:

    div(*inner_tags)
        Create div tag.

        Parameters
        ----------
        *inner_tags
            Children tags.

Documentation has exactly the same syntax as classes. The only main difference is that currently function can inherit just from a single function. It won't work if you try to wrap function with multiple decorators.

## Source Code

The main code is available [at GitHub in the NeuPy repository](https://github.com/itdxer/neupy/blob/master/neupy/core/docs.py). It's pretty simple and almost a standalone script. One dependency is a ``AttributeKeyDict`` class which is really small.

All code from the article you can find in [iPython Notebook](https://github.com/itdxer/blog.itdxer.com/blob/gh-pages/notebooks/2016-07-25%20Share%20Documentation%20Between%20Classes%20and%20Functions%20in%20Python.ipynb)
