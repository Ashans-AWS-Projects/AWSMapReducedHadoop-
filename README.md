
<!-- Markdown with Embedded HTML & CSS -->
<div style="background-color: #f7f9fc; padding: 20px; border-radius: 10px;">
    <h1 align="center" style="font-family: 'Arial', sans-serif; color: #2c3e50;">Hadoop Batch Data Processing with MapReduce, Pig, and Hive</h1>
</div>

<div align="center">
    <img src="https://user-images.githubusercontent.com/yourprofile/hadoop-banner.png" alt="Hadoop Banner" style="width: 80%; border-radius: 10px;">
</div>

<br>

## 🌟 Overview

This project showcases various batch data processing techniques using Hadoop's ecosystem, including MapReduce, Pig, and Hive, to analyze bigram data. The analysis focuses on extracting insights from a large dataset, such as identifying the most common bigrams over time, calculating average occurrences, and more.

## 📋 Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Tasks Overview](#tasks-overview)
- [Results](#results)
- [Screenshots](#screenshots)
- [Contributors](#contributors)


## 🚀 Introduction

In this project, we set up a Hadoop cluster using Amazon EMR, followed by executing various data processing tasks. The tasks include implementing custom MapReduce jobs, writing Pig scripts, and running Hive queries to gain insights from a large corpus of text data.

## 🛠️ Technologies Used

<div style="display: flex; justify-content: space-around; padding: 10px;">
    <img src="https://img.shields.io/badge/Apache%20Hadoop-66CCFF?style=for-the-badge&logo=apache&logoColor=white" alt="Apache Hadoop">
    <img src="https://img.shields.io/badge/Amazon%20EMR-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white" alt="Amazon EMR">
    <img src="https://img.shields.io/badge/Apache%20Pig-FB8333?style=for-the-badge&logo=apache&logoColor=white" alt="Apache Pig">
    <img src="https://img.shields.io/badge/Apache%20Hive-FF6F00?style=for-the-badge&logo=apache&logoColor=white" alt="Apache Hive">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</div>

## 🛠️ Setup and Installation

### Prerequisites

- **AWS Account**: To create and manage EMR clusters.
- **Python**: Install Python 3.x.
- **mrjob**: Install using pip.
  ```bash
  pip install mrjob
  ```

### Setting up Hadoop Cluster on AWS EMR

1. **Create an EMR Cluster**:
   - Use the AWS console to create a new EMR cluster.
   - Ensure that the cluster has HDFS, YARN, and applications like Pig and Hive installed.

2. **Upload Datasets to HDFS**:
   - Use the EMR master node to upload datasets to HDFS.

3. **Configure SSH**:
   - Enable SSH access to the master node for running jobs.

4. **Install Dependencies**:
   - Install `mrjob` on the master node using pip.
   - Ensure Hadoop and its components are correctly set up.

## 📝 Tasks Overview

### 1. Word Count with MapReduce (Python)
Implemented a MapReduce job to count the occurrences of each word in a large text file.

**Command to run**:
```bash
python wordcount-mr.py -r hadoop hdfs:///user/ashan/book.txt --output-dir=hdfs:///user/ashan/wordcountoutput --conf-path=mrjob.conf
```

### 2. Bigram Analysis
This project contains several bigram analysis tasks, including:
- **Challenge 1**: Find bigrams that first appeared after 1992.
- **Challenge 2**: Calculate the average occurrence of each bigram across all years.
- **Challenge 3**: Determine the most common bigram in the year 2003.
- **Challenge 4**: Identify the most common bigram for each year.
- **Challenge 5**: Use Hive to find the most popular bigram over all years.

### 3. Word Count with Pig
Used Pig to perform word count operations on the dataset.

**Command to run**:
```bash
pig wordcount-pig.txt
```

### 4. Bigram Analysis with Hive
Ran a Hive query to determine the most popular bigram over all years.

**Hive Query**:
```sql
SELECT bigram, SUM(wordcount) AS total_count
FROM `default`.`hue__tmp_challenge5`
WHERE size(split(bigram, ' ')) > 0
GROUP BY bigram
ORDER BY total_count DESC
LIMIT 1;
```

## 📊 Results

- **Word Count**: Detailed word count results for the input text.
- **Bigram Analysis**: Insightful results on the most common bigrams, their averages, and their occurrences over time.
- **Pig Output**: Stored results in HDFS, showcasing the processing done using Pig scripts.

## 📸 Screenshots

### Hive Query Execution
<div align="center">
    <img src="https://user-images.githubusercontent.com/yourprofile/hive_query_screenshot.png" alt="Hive Query Execution" style="border-radius: 10px; box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);">
</div>

## 👥 Contributors

- **Ryan Britton**
- **Ashan Deen**


3. **Host Images**: If you don't have a hosting service, upload your images directly to your GitHub repository and link them.

This enhanced `README.md` not only looks professional but also demonstrates your ability to present technical work in an organized and aesthetically pleasing way—something recruiters will certainly appreciate.
