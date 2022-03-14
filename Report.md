# Agricultural Modelling Project Report

## Table of Contents

1. [Team Members and Roles](#team-members-and-roles)
2. [Application Description](#application-description)
3. [Application UML Diagrams](#application-uml-diagrams)
4. [Application Design and Decisions](#application-design-and-decisions)
5. [Summary of Known Errors and Bugs](#summary-of-known-errors-and-bugs)
6. [Testing Summary](#testing-summary)
7. [Implemented Features](#implemented-features)


## Team Members and Roles

| UID | Name | Role |
| :--- | :----: | ---: |
| [u7292446] | [Tian Zhao] | [Project manager] |
| [u7234659] | [Hong Gic Oh] | [Developer] |
| [u7323912] | [Xuanchen Wang] | [Developer] |
| [u7292446] | [Danfeng Huang] | [Developer] |
| [u7239623] | [Zhidong Zhong] | [Developer] |
| [u7212626] | [Yancheng Yu] | [Developer] |


## Application Description

*[What is your application, what does it do? Include photos or diagrams if necessary]*

*Here is a pet specific social media application example*

*Diary Pal is a social media application that can help people post your thoughts and connect to the world. In this app, Users can post their sentences. Users can like other people's posts.
*

**Application Use Cases and or Examples**

*[Provide use cases and examples of people using your application. Who are the target users of your application? How do the users use your application?]*

*Here is a pet training application example*

*Molly wants to inquiry about her cat, McPurr's recent troublesome behaviour*
1. *Molly notices that McPurr has been hostile since...*
2. *She makes a post about... with the tag...*
3. *Lachlan, a vet, writes a reply to Molly's post...*
4. ...
5. *Molly gives Lachlan's reply a 'tick' response*

*Here is a map navigation application example*

*Targets Users: Drivers*

* *Users can use it to navigate in order to reach the destinations.*
* *Users can learn the traffic conditions*
* ...

*Target Users: Those who want to find some good restaurants*

* *Users can find nearby restaurants and the application can give recommendations*
* ...

*List all the use cases in text descriptions or create use case diagrams. Please refer to https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-use-case-diagram/ for use case diagram.*

## Application UML Diagrams

![ClassDiagramExample](./images/ClassDiagramExample.png)
*[Replace the above with a class diagram. You can look at how we have linked an image here as an example of how you can do it too.]*

## Application Design and Decisions

*Please give clear and concise descriptions for each subsections of this part. It would be better to list all the concrete items for each subsection and give no more than `5` concise, crucial reasons of your design. Here is an example for the subsection `Data Structures`:*

*I used the following data structures in my project:*

1. *LinkedList*

   * *Objective: It is used for storing xxxx for xxx feature.*

   * *Locations: line xxx in XXX.java, ..., etc.*

   * *Reasons:*

     * *It is more efficient than Arraylist for insertion with a time complexity O(1)*

     * *We don't need to access the item by index for this feature*

2. ...

3. ...

**Data Structures**

*[What data structures did your team utilise? Where and why?]*

**Design Patterns**

*[What design patterns did your team utilise? Where and why?]*
*1. DAO patterns, this project we use firebase to store users' information and chat data. DAO makes us hava a much more simple way to assess data without using specific method(e.g. @query)*
*2. MVVM, this structral design pattern is used often in our project(e.g. chatpage, friend request), it separates models and views, meanwhile aviod massive view controller. *
**Grammars**

*Search Engine*
<br> *Production Rules* <br>
\<Non-Terminal> ::= \<some output>
<br>
\<Non-Terminal> ::= \<some output>

*[How do you design the grammar? What are the advantages of your designs?]*

*If there are several grammars, list them all under this section and what they relate to.*

**Tokenizer and Parsers**

*[Where do you use tokenisers and parsers? How are they built? What are the advantages of the designs?]*

**Surpise Item**

*[If you implement the surprise item, explain how your solution addresses the surprise task. What decisions do your team make in addressing the problem?]*

**Other**

*[What other design decisions have you made which you feel are relevant? Feel free to separate these into their own subheadings.]*

## Summary of Known Errors and Bugs

*[Where are the known errors and bugs? What consequences might they lead to?]*

*Here is an example:*

1. *Bug 1:*

- *A space bar (' ') in the sign in email will crash the application.*
- ... 

2. *Bug 2:*
3. ...

*List all the known errors and bugs here. If we find bugs/errors that your team do not know of, it shows that your testing is not through.*

## Testing Summary

*[What features have you tested? What is your testing coverage?]*

*Here is an example:*

*Number of test cases: ...*

*Code coverage: ...*

*Types of tests created: ...*

*Please provide some screenshots of your testing summary, showing the achieved testing coverage. Feel free to provide further details on your tests.*

## Implemented Features

*[What features have you implemented?]*

*Here is an example:*

*User Privacy*

1. *Friendship. Users may send friend requests which are then accepted or denied. (easy)*
2. *Privacy I: A user must approve a friend's request based on privacy settings. (easy)*
3. *Privacy II: A user can only see a profile that is Public (consider that there are at least two types of profiles: public and private). (easy)*
4. *Privacy III: A user can only follow someone who shares at least one mutual friend based on privacy settings. (Medium)*

*Firebase Integration*
1. *Use Firebase to implement user Authentication/Authorisation. (easy)*
2. *Use Firebase to persist all data used in your app (this item replace the requirement to retrieve data from a local file) (medium)*

*List all features you have completed in their separate categories with their difficulty classification. If they are features that are suggested and approved, please state this somewhere as well.*

