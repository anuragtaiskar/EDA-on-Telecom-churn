{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "private_outputs": true,
      "provenance": [],
      "collapsed_sections": [
        "vncDsAP0Gaoa",
        "FJNUwmbgGyua",
        "w6K7xa23Elo4",
        "yQaldy8SH6Dl",
        "PH-0ReGfmX4f",
        "mDgbUHAGgjLW",
        "O_i_v8NEhb9l",
        "HhfV-JJviCcP",
        "Y3lxredqlCYt",
        "3RnN4peoiCZX",
        "x71ZqKXriCWQ",
        "7hBIi_osiCS2",
        "JlHwYmJAmNHm",
        "35m5QtbWiB9F",
        "PoPl-ycgm1ru",
        "H0kj-8xxnORC",
        "nA9Y7ga8ng1Z",
        "PBTbrJXOngz2",
        "u3PMJOP6ngxN",
        "dauF4eBmngu3",
        "bKJF3rekwFvQ",
        "MSa1f5Uengrz",
        "GF8Ens_Soomf",
        "0wOQAZs5pc--",
        "K5QZ13OEpz2H",
        "lQ7QKXXCp7Bj",
        "448CDAPjqfQr",
        "KSlN3yHqYklG",
        "t6dVpIINYklI",
        "ijmpgYnKYklI",
        "-JiQyfWJYklI",
        "EM7whBJCYoAo",
        "fge-S5ZAYoAp",
        "85gYPyotYoAp",
        "RoGjAbkUYoAp",
        "4Of9eVA-YrdM",
        "iky9q4vBYrdO",
        "F6T5p64dYrdO",
        "y-Ehk30pYrdP",
        "bamQiAODYuh1",
        "QHF8YVU7Yuh3",
        "GwzvFGzlYuh3",
        "qYpmQ266Yuh3",
        "OH-pJp9IphqM",
        "bbFf2-_FphqN",
        "_ouA3fa0phqN",
        "Seke61FWphqN",
        "PIIx-8_IphqN",
        "t27r6nlMphqO",
        "r2jJGEOYphqO",
        "b0JNsNcRphqO",
        "BZR9WyysphqO",
        "jj7wYXLtphqO",
        "eZrbJ2SmphqO",
        "rFu4xreNphqO",
        "YJ55k-q6phqO",
        "gCFgpxoyphqP",
        "OVtJsKN_phqQ",
        "lssrdh5qphqQ",
        "U2RJ9gkRphqQ",
        "1M8mcRywphqQ",
        "tgIPom80phqQ",
        "JMzcOPDDphqR",
        "x-EpHcCOp1ci",
        "X_VqEhTip1ck",
        "8zGJKyg5p1ck",
        "PVzmfK_Ep1ck",
        "n3dbpmDWp1ck",
        "ylSl6qgtp1ck",
        "ZWILFDl5p1ck",
        "M7G43BXep1ck",
        "Ag9LCva-p1cl",
        "E6MkPsBcp1cl",
        "2cELzS2fp1cl",
        "3MPXvC8up1cl",
        "NC_X3p0fY2L0",
        "UV0SzAkaZNRQ",
        "YPEH6qLeZNRQ",
        "q29F0dvdveiT",
        "EXh0U9oCveiU",
        "22aHeOlLveiV",
        "JcMwzZxoAimU",
        "8G2x9gOozGDZ",
        "gCX9965dhzqZ",
        "gIfDvo9L0UH2"
      ],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/anuragtaiskar/EDA-on-Telecom-churn/blob/main/EDA_On_Telecom_churn.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Project Name**    - \n",
        "\n"
      ],
      "metadata": {
        "id": "vncDsAP0Gaoa"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### **Project Type**    - EDA\n",
        "##### **Contribution**    - Individual\n",
        "##### **Name** - Anurag Taiskar"
      ],
      "metadata": {
        "id": "beRrZCGUAJYm"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Project Summary -**"
      ],
      "metadata": {
        "id": "FJNUwmbgGyua"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Telecom churn analysis is the process of identifying customers who are likely to cancel their service or switch to a different service provider. This is an important problem for telecom companies, as churn can have a significant impact on their revenue and profitability. Orange Telecom's Churn Dataset consists of cleaned customer activity data and a label specifying whether a customer has churned. The goal of the analysis is to understand the factors that contribute to churn and develop strategies to reduce churn by targeting those factors. The first step in conducting an exploratory data analysis (EDA) for telecom churn analysis is data acquisition, which involves obtaining a representative sample of data from the telecom company including customer demographic information, usage patterns, and churn status. The next step is data cleaning, which involves removing any missing or incomplete data and ensuring that the data is in a format that can be easily analyzed. Data visualization involves using plots and charts to visualize the data and identify trends and patterns, while data summarization involves using statistical techniques to summarize the data and understand the relationships between different variables.\n",
        "\n",
        "To reduce churn and improve customer retention, it is important to take a proactive approach. One effective strategy is to modify the International Plan so that the charges are the same as the normal plan. This will help address any potential dissatisfaction with higher charges for international usage. Communication and asking for feedback often can help to identify and address any issues that may lead to churn. Offering promotions periodically can also help to retain customers, as can focusing on customers experiencing problems in states with high churn rates. Paying attention to your best customers and ensuring they receive the support they need is also important. Regular server maintenance and addressing poor network connectivity issues can also help to reduce churn. Developing a roadmap for onboarding new customers can help to ensure a smooth onboarding process and reduce the likelihood of churn. Analyzing churn when it occurs can provide valuable insights into the factors contributing to churn, which can inform strategies for reducing churn. Finally, it is important to stay competitive by keeping up with industry trends and continuously improving the customer experience.\n",
        "\n",
        "Through EDA of the churn dataset, it was found that the charge fields are directly related to the minute fields, the area code may not be relevant and can be excluded, customers with the International Plan tend to churn more often, customers who have had four or more customer service calls churn significantly more than other customers, customers with high day and evening minute usage tend to churn at a higher rate, and there is no clear relationship between churn and the number of calls made or received. In conclusion, to reduce churn and improve customer retention, telecom companies should focus on modifying the International Plan, being proactive with communication and asking for feedback, offering promotions, focusing on customers experiencing problems in states with high churn rates, paying attention to their best customers, and continuously improving the customer experience."
      ],
      "metadata": {
        "id": "F6v_1wHtG2nS"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **GitHub Link -**"
      ],
      "metadata": {
        "id": "w6K7xa23Elo4"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "https://github.com/anuragtaiskar/EDA-on-Telecom-churn"
      ],
      "metadata": {
        "id": "h1o69JH3Eqqn"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Problem Statement**\n"
      ],
      "metadata": {
        "id": "yQaldy8SH6Dl"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Telecom churn analysis is the process of identifying customers who are likely to cancel their service or switch to a different service provider. This is an important problem for telecom companies, as churn can have a significant impact on their revenue and profitability.\n",
        "\n",
        "Orange S.A., formerly France Télécom S.A., is a French multinational telecommunications corporation. The Orange Telecom's Churn Dataset, consists of cleaned customer activity data (features), along with a churn label specifying whether a customer canceled the subscription. Explore and analyze the data to discover key factors responsible for customer churn and come up with ways/recommendations to ensure customer retention."
      ],
      "metadata": {
        "id": "DpeJGUA3kjGy"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### **Define Your Business Objective?**"
      ],
      "metadata": {
        "id": "PH-0ReGfmX4f"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Identifying the key cause of the customer churn\n",
        "\n",
        "*provide steps to retain the valuable customer"
      ],
      "metadata": {
        "id": "PhDvGCAqmjP1"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **General Guidelines** : -  "
      ],
      "metadata": {
        "id": "mDgbUHAGgjLW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1.   Well-structured, formatted, and commented code is required. \n",
        "2.   Exception Handling, Production Grade Code & Deployment Ready Code will be a plus. Those students will be awarded some additional credits. \n",
        "     \n",
        "     The additional credits will have advantages over other students during Star Student selection.\n",
        "       \n",
        "             [ Note: - Deployment Ready Code is defined as, the whole .ipynb notebook should be executable in one go\n",
        "                       without a single error logged. ]\n",
        "\n",
        "3.   Each and every logic should have proper comments.\n",
        "4. You may add as many number of charts you want. Make Sure for each and every chart the following format should be answered.\n",
        "        \n",
        "\n",
        "```\n",
        "# Chart visualization code\n",
        "```\n",
        "            \n",
        "\n",
        "*   Why did you pick the specific chart?\n",
        "*   What is/are the insight(s) found from the chart?\n",
        "* Will the gained insights help creating a positive business impact? \n",
        "Are there any insights that lead to negative growth? Justify with specific reason.\n",
        "\n",
        "5. You have to create at least 20 logical & meaningful charts having important insights.\n",
        "\n",
        "\n",
        "[ Hints : - Do the Vizualization in  a structured way while following \"UBM\" Rule. \n",
        "\n",
        "U - Univariate Analysis,\n",
        "\n",
        "B - Bivariate Analysis (Numerical - Categorical, Numerical - Numerical, Categorical - Categorical)\n",
        "\n",
        "M - Multivariate Analysis\n",
        " ]\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "ZrxVaUj-hHfC"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# ***Let's Begin !***"
      ],
      "metadata": {
        "id": "O_i_v8NEhb9l"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## ***1. Know Your Data***"
      ],
      "metadata": {
        "id": "HhfV-JJviCcP"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Import Libraries"
      ],
      "metadata": {
        "id": "Y3lxredqlCYt"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Import Libraries\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "# Import Visualization Libraries\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "%matplotlib inline\n",
        "\n",
        "# Import warnings\n",
        "import warnings\n",
        "warnings.filterwarnings('ignore')"
      ],
      "metadata": {
        "id": "M8Vqi-pPk-HR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Dataset Loading"
      ],
      "metadata": {
        "id": "3RnN4peoiCZX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Load Dataset\n",
        "from google.colab import drive\n",
        "drive.mount('/content/drive')\n",
        "churn_df=pd.read_csv('/content/drive/MyDrive/EDA on telecom churn/Telecom Churn.csv')"
      ],
      "metadata": {
        "id": "4CkvbW_SlZ_R"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Dataset First View"
      ],
      "metadata": {
        "id": "x71ZqKXriCWQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Display first 10 indexes of the dataset\n",
        "churn_df.head(10)"
      ],
      "metadata": {
        "id": "McK-cC90dnhi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Display last 10 indexes of the dataset\n",
        "churn_df.tail(10)"
      ],
      "metadata": {
        "id": "LWNFOSvLl09H"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Dataset Rows & Columns count"
      ],
      "metadata": {
        "id": "7hBIi_osiCS2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Dataset Rows & Columns count\n",
        "#below given code returns a tuple representing the dimensionality of the DataFrame.\n",
        "print(churn_df.shape)\n",
        "print(\"Number of rows are: \",churn_df.shape[0])\n",
        "print(\"Number of columns are: \",churn_df.shape[1])"
      ],
      "metadata": {
        "id": "Kllu7SJgmLij"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Dataset Information"
      ],
      "metadata": {
        "id": "JlHwYmJAmNHm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Dataset Info\n",
        "churn_df.info()"
      ],
      "metadata": {
        "id": "e9hRXRi6meOf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Duplicate Values"
      ],
      "metadata": {
        "id": "35m5QtbWiB9F"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Dataset Duplicate Value Count\n",
        "churn_df.duplicated().sum()"
      ],
      "metadata": {
        "id": "1sLdpKYkmox0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Missing Values/Null Values"
      ],
      "metadata": {
        "id": "PoPl-ycgm1ru"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Missing Values/Null Values Count\n",
        "churn_df.isnull().sum()"
      ],
      "metadata": {
        "id": "GgHWkxvamxVg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Visualizing the missing values\n",
        "No missing value present.Hence, no need to do the missing value imputation"
      ],
      "metadata": {
        "id": "X4LtQrqQiVJ_"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### What did you know about your dataset?"
      ],
      "metadata": {
        "id": "H0kj-8xxnORC"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "This dataset is from telecom industry. There is threat to the company when customer churn happens. We have to analyze the customer churn and insights of it. And determine why the customer churn is happening.\n",
        "\n",
        "In this dataset, there are 3333 number of rows and 20 feature columns. Also there are no missing values and duplicate values in dataset."
      ],
      "metadata": {
        "id": "gfoNAAC-nUe_"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## ***2. Understanding Your Variables***"
      ],
      "metadata": {
        "id": "nA9Y7ga8ng1Z"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Dataset Columns\n",
        "columns_list=list(churn_df.columns)\n",
        "print(columns_list)"
      ],
      "metadata": {
        "id": "j7xfkqrt5Ag5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Dataset Describe\n",
        "churn_df.describe()"
      ],
      "metadata": {
        "id": "DnOaZdaE5Q5t"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Variables Description "
      ],
      "metadata": {
        "id": "PBTbrJXOngz2"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "State : Categorica for the 50 states and capital DC.\n",
        "\n",
        "Account Length : Number of days account has been active.\n",
        "\n",
        "Area Code : Code Number of Area having some States included in each area code.\n",
        "\n",
        "lnternational Plan : International Plan activated ( yes, no )\n",
        "\n",
        "Voice Mail Plan : Voice Mail Plan activated ( yes ,no )\n",
        "\n",
        "Voice Mail Message : Count of vmail messages sent.\n",
        "\n",
        "Day Minutes : Total minutes uesd during day time\n",
        "\n",
        "Day calls : Total number of calls during day time\n",
        "\n",
        "Day Charge : Total charge during day time\n",
        "\n",
        "Evening Minutes : Total minutes used during evening time\n",
        "\n",
        "Evening Calls : Total number of calls during evening time\n",
        "\n",
        "Evening Charge : Total charge during evening time\n",
        "\n",
        "Night Minutes : Total minutes used during night time\n",
        "\n",
        "Night Calls : Total number of calls during night time\n",
        "Night Charge : Total charge during night time\n",
        "\n",
        "International Minutes : Total minutes used of international call\n",
        "\n",
        "International Calls : Total number of international calls\n",
        "\n",
        "International Charge : Total charge of international calls\n",
        "\n",
        "Customer Service calls : Number of calls to customer service\n",
        "\n",
        "Churn :Customer churn (Target Variable True=1, False=0)"
      ],
      "metadata": {
        "id": "aJV4KIxSnxay"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Check Unique Values for each variable."
      ],
      "metadata": {
        "id": "u3PMJOP6ngxN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Check Unique Values for each variable.\n",
        "for i in columns_list:\n",
        "  print(\"No. of unique values in\",i,\"is\",churn_df[i].nunique())"
      ],
      "metadata": {
        "id": "zms12Yq5n-jE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 3. ***Data Wrangling***"
      ],
      "metadata": {
        "id": "dauF4eBmngu3"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Data Wrangling Code"
      ],
      "metadata": {
        "id": "bKJF3rekwFvQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Churn by each columns\n",
        "churn_count1 = churn_df.groupby('Churn')\n",
        "churn_count1.mean()"
      ],
      "metadata": {
        "id": "izSdvjrerTtC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#calculate charges for each kind of mins:\n",
        "day_min_charges = churn_df['Total day charge'].mean()/churn_df['Total day minutes'].mean()\n",
        "eve_min_charges = churn_df['Total eve charge'].mean()/churn_df['Total eve minutes'].mean()\n",
        "night_min_charges = churn_df['Total night charge'].mean()/churn_df['Total night minutes'].mean()\n",
        "int_min_charges= churn_df['Total intl charge'].mean()/churn_df['Total intl minutes'].mean()\n",
        "print(f' Day_min_charge: {day_min_charges}')\n",
        "print(f'eve_min_charge: {eve_min_charges}')\n",
        "print(f'night_min_charge: {night_min_charges}')\n",
        "print(f'Total intl charge: {int_min_charges}') "
      ],
      "metadata": {
        "id": "gK6-KKvSfvCk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# percentage of customer churned out of total customer statewise\n",
        "State_data = pd.crosstab(churn_df[\"State\"],churn_df[\"Churn\"])\n",
        "State_data['Churn_%'] = State_data.apply(lambda x : x[1]*100/(x[0]+x[1]),\n",
        "                                         axis = 1)\n",
        "print(State_data)"
      ],
      "metadata": {
        "id": "-Bf5CE5SlD48"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# percentage of customer who churned with respect to total no of cusmtomers witn international plan ON & OFF\n",
        "International_plan = pd.crosstab(churn_df[\"International plan\"],churn_df[\"Churn\"])\n",
        "International_plan['Churn_%'] = International_plan.apply(lambda x : x[1]*100/(x[0]+x[1]),axis = 1)\n",
        "print(International_plan)"
      ],
      "metadata": {
        "id": "Y81v4ePDxa2Y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# churn rate area code wise\n",
        "churn_area = pd.DataFrame(churn_df.groupby('Area code')['Churn'].value_counts())\n",
        "churn_area['churn rate'] = round(churn_area*100/len(churn_df),2)\n",
        "churn_area\n",
        "  "
      ],
      "metadata": {
        "id": "cSLllFcYty3R"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#churn rate for customer with and without voice mail paln\n",
        "Voice_mail = pd.crosstab(churn_df[\"Voice mail plan\"],churn_df[\"Churn\"])\n",
        "Voice_mail['Churn_%'] = Voice_mail.apply(lambda x : x[1]*100/(x[0]+x[1]),axis = 1)\n",
        "print(Voice_mail)"
      ],
      "metadata": {
        "id": "DfGxASscvozC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### What all manipulations have you done and insights you found?"
      ],
      "metadata": {
        "id": "MSa1f5Uengrz"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**customer churned out of total customer statewise**\n",
        "\n",
        "From the above analysis( CA, NJ, TX, MD, SC, MI ) are the ones with churn rate of higher than 21.\n",
        "As we can see not all state have approximately same churn , thus package price(charges) cannnot be major factor . The reason for churn rate from a particular state may be due to the low coverage of the cellular network.\n",
        "\n",
        "**Churn on basis of international plan**\n",
        "\n",
        "In this we found out that those who has international plan their churn rate is higher, almost 42.41 % customers are churned.\n",
        "\n",
        "**churn on basis of international plan**\n",
        "\n",
        "we can see their is no clear relation that we can find between the customers with voice maill plan vs. people who churned \n",
        "\n"
      ],
      "metadata": {
        "id": "LbyXE7I1olp8"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## ***4. Data Vizualization, Storytelling & Experimenting with charts : Understand the relationships between variables***"
      ],
      "metadata": {
        "id": "GF8Ens_Soomf"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Chart - 1"
      ],
      "metadata": {
        "id": "0wOQAZs5pc--"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# pie chart of churn column(in percentage)\n",
        "data = churn_df['Churn'].value_counts()\n",
        "explode = (0, 0.2)\n",
        "plt.pie(data, explode = explode,autopct='%1.1f%%',shadow=True,radius = 3.0, \n",
        "        labels = ['Not churned customer','Churned customer'],\n",
        "        colors=['green' ,'red'])\n",
        "circle = plt.Circle( (0,0), 1, color='white')"
      ],
      "metadata": {
        "id": "7v_ESjsspbW7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 1. Why did you pick the specific chart?"
      ],
      "metadata": {
        "id": "K5QZ13OEpz2H"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Pie charts are especially useful for displaying data that has already been calculated as a percentage of the whole."
      ],
      "metadata": {
        "id": "XESiWehPqBRc"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 2. What is/are the insight(s) found from the chart?"
      ],
      "metadata": {
        "id": "lQ7QKXXCp7Bj"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "There are 2850 customers which are not churned which is 85.5% of the total customers dataset and 483 customers are churned which is 14.5 % of the whole customers data given in the dataset. "
      ],
      "metadata": {
        "id": "C_j1G7yiqdRP"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 3. Will the gained insights help creating a positive business impact? \n",
        "Are there any insights that lead to negative growth? Justify with specific reason."
      ],
      "metadata": {
        "id": "448CDAPjqfQr"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "It's easy to loose customers but too difficult to aquire one. One churned cutomer will make 3-4 customers away those might be acquired by your teleservice provider.So, definitely churn rate insight is very helpful for further decisions."
      ],
      "metadata": {
        "id": "3cspy4FjqxJW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Chart - 2"
      ],
      "metadata": {
        "id": "KSlN3yHqYklG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Histogram for each variable\n",
        "churn_df.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)"
      ],
      "metadata": {
        "id": "R4YgtaqtYklH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 1. Why did you pick the specific chart?"
      ],
      "metadata": {
        "id": "t6dVpIINYklI"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "A histplot is a type of chart that displays the distribution of a dataset. It is a graphical representation of the data that shows how often each value or group of values occurs. Histplots are useful for understanding the distribution of a dataset and identifying patterns or trends in the data. It is also useful when dealing with large data sets (greater than 100 observations). It can help detect any unusual observations (outliers) or any gaps in the data.I used the histogram plot to analysis the variable distributions over the whole dataset whether it's symmetric or not."
      ],
      "metadata": {
        "id": "5aaW0BYyYklI"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 2. What is/are the insight(s) found from the chart?"
      ],
      "metadata": {
        "id": "ijmpgYnKYklI"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "All columns are symmetric distributed and mean is nearly same with median for numerical columns. Here Area code will be treated as categorical value as there are only 3 values in the particular column."
      ],
      "metadata": {
        "id": "PSx9atu2YklI"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 3. Will the gained insights help creating a positive business impact? \n",
        "Are there any insights that lead to negative growth? Justify with specific reason."
      ],
      "metadata": {
        "id": "-JiQyfWJYklI"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Histogram can not give us whole information regarding data.It's only used for overlooking the distribution of the column data over the dataset."
      ],
      "metadata": {
        "id": "BcBbebzrYklV"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Chart - 3"
      ],
      "metadata": {
        "id": "EM7whBJCYoAo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Vizualizing Total day minutes vs total day charge\n",
        "sns.scatterplot(x=\"Total day minutes\", y=\"Total day charge\", hue=\"Churn\", \n",
        "                data=churn_df)"
      ],
      "metadata": {
        "id": "t6GMdE67YoAp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Vizualizing Total eve minutes vs total eve charge\n",
        "sns.scatterplot(x=\"Total eve minutes\", y=\"Total eve charge\", hue=\"Churn\", \n",
        "                data=churn_df)"
      ],
      "metadata": {
        "id": "EjxfuRGn8diw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Vizualizing Total night minutes vs total night charge\n",
        "sns.scatterplot(x=\"Total night minutes\", y=\"Total night charge\", hue=\"Churn\", \n",
        "                data=churn_df)"
      ],
      "metadata": {
        "id": "dWpCHQ9H9Y5d"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 1. Why did you pick the specific chart?"
      ],
      "metadata": {
        "id": "fge-S5ZAYoAp"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Scatter plots are used to plot the relationship between two numerical variables. Scatter plots are useful for identifying patterns and trends in data, and they can be used to visualize the relationship between two variables.\n",
        "we have used the scatter plot to depict the relationship between evening, day & night calls , minutes and charge."
      ],
      "metadata": {
        "id": "5dBItgRVYoAp"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 2. What is/are the insight(s) found from the chart?"
      ],
      "metadata": {
        "id": "85gYPyotYoAp"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Churn customers speak more minutes that non-churn customers at day,evening and night. Hence they pay more charge that non-churn customers.\n",
        "\n",
        "We can retain churn customers if we include master plan. In master plan if a customer is talking more minutes then we can charge a little less amount from him or he can get discount or additional few free minutes to talk.\n",
        "\n",
        "This will make customers who are going to churn happy and they will not leave the company."
      ],
      "metadata": {
        "id": "4jstXR6OYoAp"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 3. Will the gained insights help creating a positive business impact? \n",
        "Are there any insights that lead to negative growth? Justify with specific reason."
      ],
      "metadata": {
        "id": "RoGjAbkUYoAp"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "For telecom service provider calling and messaging are two essential product plans. Thus, optimizing voice call plans will definitely create a business impact. Those who are using just calling service must be provided some additional offers either in talktime or powerplus plan. Those who use voice call plan for night only, we might offer some exciting plans from midnight 12 to morning 6. For customers those who have higher accout length should be provided exciting offers as they are our loyal customers. Churing of higher account length customer will have a negative impact on business."
      ],
      "metadata": {
        "id": "zfJ8IqMcYoAp"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Chart - 4"
      ],
      "metadata": {
        "id": "4Of9eVA-YrdM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Customer Service Calls \n",
        "pd.crosstab(churn_df['Churn'], churn_df[\"Customer service calls\"], margins=True)"
      ],
      "metadata": {
        "id": "gn1lfJz0F0Qm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Histogram of Customer Serice calls grouped by churn  \n",
        "plt.rcParams['figure.figsize'] = (8, 6)\n",
        "sns.countplot(x=\"Customer service calls\", hue='Churn', data=churn_df);"
      ],
      "metadata": {
        "id": "VuIEcaNRFzYl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 1. Why did you pick the specific chart?"
      ],
      "metadata": {
        "id": "iky9q4vBYrdO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Count plot are used to compare the size or frequency of different categories or groups of data. Bar charts are useful for comparing data across different categories, and they can be used to display a large amount of data in a small space.we have used the bar plot to show the relationship between churn rate per customer service calls."
      ],
      "metadata": {
        "id": "aJRCwT6DYrdO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 2. What is/are the insight(s) found from the chart?"
      ],
      "metadata": {
        "id": "F6T5p64dYrdO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "The service calls of customers varies from 0 to 9 .\n",
        "\n",
        "Those customers who make more service calls they have a high probability of leaving.\n",
        "\n",
        "As we can see from graph , customers with more than 5, their churning rate is more.\n",
        "\n",
        "Hence customers who make more than 5 service calls, their queries should be solved immediately and they should be given better service so that they dont leave the company.\n",
        "\n",
        "Customers with four or more customer service calls churn more than four times as often as do the other customers"
      ],
      "metadata": {
        "id": "Xx8WAJvtYrdO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 3. Will the gained insights help creating a positive business impact? \n",
        "Are there any insights that lead to negative growth? Justify with specific reason."
      ],
      "metadata": {
        "id": "y-Ehk30pYrdP"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Customer service is an essential factor for every business. So definitely good customer service will have a positive impact to the business. We have to look after the customer calls and customer query report resolution duration. Need to optimize the time period. If one type of issue is coming from more than 5 customers, root cause analysis should be done on that same issue and should be resolved for everyone. Need to reduce the calls for each customer and he should be satisfied in a single call only. The customer service agents should be given great offer or recognition over great performance of customer issue resolution."
      ],
      "metadata": {
        "id": "jLNxxz7MYrdP"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Chart - 5"
      ],
      "metadata": {
        "id": "bamQiAODYuh1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# statewise data regarding the no. of churned and not churned customers\n",
        "sns.set(style=\"darkgrid\")                                                    \n",
        "plt.figure(figsize=(15,8))\n",
        "ax = sns.countplot(x='State', hue=\"Churn\", data=churn_df)\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "TIJwrbroYuh3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 1. Why did you pick the specific chart?"
      ],
      "metadata": {
        "id": "QHF8YVU7Yuh3"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Count plot are used to compare the size or frequency of different categories or groups of data. Count plot are useful for comparing data across different categories, and they can be used to display a large amount of data in a small space.To show the average percentage of true churn with respect to states, we have used Count plot."
      ],
      "metadata": {
        "id": "dcxuIMRPYuh3"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 2. What is/are the insight(s) found from the chart?"
      ],
      "metadata": {
        "id": "GwzvFGzlYuh3"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "There are 51 states having different churn rates .\n",
        "\n",
        "CA, NJ ,TX , MD ,SC ,MI, MS, NV, WA, ME are the ones who have higher churn rate more than 20% which is more than 50% of average churn rate.\n",
        "\n",
        "And HI, AK, AZ, VA, IA, LA, NE, IL, WI, RI are the ones who have lower churn rate which is less than 10%."
      ],
      "metadata": {
        "id": "uyqkiB8YYuh3"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 3. Will the gained insights help creating a positive business impact? \n",
        "Are there any insights that lead to negative growth? Justify with specific reason."
      ],
      "metadata": {
        "id": "qYpmQ266Yuh3"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Are there any insights that lead to negative growth? Justify with specific reason.\n",
        "\n",
        "Yes, the data of state wise churning depicts that there are lot of states who are having average churn rate more than 20 % which needs to be studied and look for further analysis to decide which factor are causing the churn."
      ],
      "metadata": {
        "id": "_WtzZ_hCYuh4"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Chart - 6"
      ],
      "metadata": {
        "id": "OH-pJp9IphqM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#One Digit Account Length \n",
        "one_length = churn_df[churn_df['Account length']<=9].loc[:,['Churn']].value_counts()\n",
        "print(one_length)\n",
        "print(\" \")\n",
        "\n",
        "# Visualizing One Digit Account Length Based on Churn percentage\n",
        "#color palette selection\n",
        "colors = sns.color_palette('pastel')[0:7]\n",
        "textprops = {'fontsize':13}\n",
        "\n",
        "plt.figure(figsize=(15,7))\n",
        "# plotting pie chart\n",
        "plt.pie(one_length, labels=['Not Churn(%)','Churn(%)'], startangle=90, colors=('green','red'), autopct=\"%1.1f%%\",textprops = textprops)\n",
        "plt.title('One Digit Account Length churn rate', fontsize=18)\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "VLJ6ghg8jha1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Two Digit Account Length \n",
        "two_account=churn_df[(churn_df['Account length']<=99) & (churn_df['Account length']>=10)].loc[:,['Churn']].value_counts()\n",
        "print(two_account)\n",
        "print(\" \")\n",
        "\n",
        "# Visualizing Two Digit Account Length Based on Churn percentage\n",
        "#color palette selection\n",
        "colors = sns.color_palette('pastel')[0:7]\n",
        "textprops = {'fontsize':13}\n",
        "\n",
        "plt.figure(figsize=(15,7))\n",
        "# plotting pie chart\n",
        "plt.pie(two_account, labels=['Not Churn(%)','Churn(%)'], startangle=90, colors=('green','red'), autopct=\"%1.1f%%\", textprops = textprops)\n",
        "plt.title('Two Digit Account Length churn rate', fontsize=18)\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "7LrUFFJIjhSe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Three Digit Account Length \n",
        "three_account=churn_df[(churn_df['Account length']<=churn_df['Account length'].max()) & (churn_df['Account length']>=100)].loc[:,['Churn']].value_counts()\n",
        "print(three_account)\n",
        "print(\" \")\n",
        "\n",
        "# Visualizing Three Digit Account Length Based on Churn percentage\n",
        "#color palette selection\n",
        "colors = sns.color_palette('pastel')[0:7]\n",
        "textprops = {'fontsize':13}\n",
        "\n",
        "plt.figure(figsize=(15,7))\n",
        "# plotting data on chart using seaborn\n",
        "plt.pie(three_account, labels=['Not Churn(%)','Churn(%)'],startangle=90 , colors=('green','red'), autopct=\"%1.1f%%\",textprops = textprops)\n",
        "plt.title('Three Digit Account Length churn rate', fontsize=18)\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "hP1CYImIjhF_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Box Plot for Account Length attribute\n",
        "plt.figure(figsize=(10,8))\n",
        "sns.boxplot(data=churn_df, x='Churn', y='Account length', showmeans = True)\n",
        "plt.title('Account Length Boxplot with Churn', fontsize=18)\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "lVPxG1qyl-6l"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 1. Why did you pick the specific chart?"
      ],
      "metadata": {
        "id": "bbFf2-_FphqN"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Pie charts are generally used to show the proportions of a whole, and are especially useful for displaying data that has already been calculated as a percentage of the whole.\n",
        "\n",
        "So, I used Pie chart and which helped me to get the percentage comparision of the churn percentage account length wise.\n",
        "\n",
        "A boxplot is used to summarize the key statistical characteristics of a dataset, including the median, quartiles, and range, in a single plot. Boxplots are useful for identifying the presence of outliers in a dataset, comparing the distribution of multiple datasets, and understanding the dispersion of the data. They are often used in statistical analysis and data visualization.\n",
        "\n",
        "So, I used box plot to get the maximum and minimum value with well sagreggated outliers with well defined mean and median as shown in the box plot graph."
      ],
      "metadata": {
        "id": "loh7H2nzphqN"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 2. What is/are the insight(s) found from the chart?"
      ],
      "metadata": {
        "id": "_ouA3fa0phqN"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "we can see that Two digit Account Length customers are churning with a number of 225 and Three digit Account Length customers are churning with a number of 256.\n",
        "\n",
        "So, their churning rate is high."
      ],
      "metadata": {
        "id": "VECbqPI7phqN"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 3. Will the gained insights help creating a positive business impact? \n",
        "Are there any insights that lead to negative growth? Justify with specific reason."
      ],
      "metadata": {
        "id": "Seke61FWphqN"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Account length is the no. of days the customers are active. So for the new customers those churning rate is too low around 8.3% in percentage and number is 2. They might be just using the telecom service to experience the benefits and they might not be satisfied with the service provided and churned.\n",
        "\n",
        "Those people whose account length are between 10 to 99 are having a churning rate of 14%. The customers below 50 might be treated as new customers and more than 55 and less than 99 they might not be geting benefits from plan taken.\n",
        "\n",
        "Those people whose account length is more than 100 are like old customers and they might be churning due to no additional offers given to them like power plus plan or other benefits.\n",
        "\n",
        "So, yes Account Length is also depicting a clear view of churing reasons and insights."
      ],
      "metadata": {
        "id": "DW4_bGpfphqN"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Chart - 7"
      ],
      "metadata": {
        "id": "PIIx-8_IphqN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# calculate count of customer with and without international plan\n",
        "churn_df['International plan'].value_counts()"
      ],
      "metadata": {
        "id": "lqAIGUfyphqO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# pie chart of percenteage of customer with international plan ON/OFF \n",
        "data = churn_df['International plan'].value_counts()\n",
        "explode = (0, 0.2)\n",
        "plt.pie(data, explode = explode,autopct='%1.1f%%',radius = 2.0, \n",
        "        labels = ['International plan: OFF','International plan: ON'],\n",
        "        colors=['skyblue' ,'orange'])\n",
        "circle = plt.Circle( (0,0), 1, color='white')\n"
      ],
      "metadata": {
        "id": "H-f20xI_m9M-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# percentage of customer who churned with respect to total no of cusmtomers witn international plan ON & OFF\n",
        "International_plan = pd.crosstab(churn_df[\"International plan\"],churn_df[\"Churn\"])\n",
        "International_plan['Churn_%'] = International_plan.apply(lambda x : x[1]*100/(x[0]+x[1]),axis = 1)\n",
        "print(International_plan)"
      ],
      "metadata": {
        "id": "O_JXaknJnjIN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Analysing by using countplot\n",
        "sns.countplot(x='International plan',hue=\"Churn\",data = churn_df)"
      ],
      "metadata": {
        "id": "g7LXl_6onZzy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 1. Why did you pick the specific chart?"
      ],
      "metadata": {
        "id": "t27r6nlMphqO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Pie charts are generally used to show the proportions of a whole, and are especially useful for displaying data that has already been calculated as a percentage of the whole.\n",
        "\n",
        "Thus, we used to show the percentage of people taken international plan through pie chart with different colored area under a circle.\n",
        "\n",
        "Bar charts are used to compare the size or frequency of different categories or groups of data. Bar charts are useful for comparing data across different categories, and they can be used to display a large amount of data in a small space"
      ],
      "metadata": {
        "id": "iv6ro40sphqO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 2. What is/are the insight(s) found from the chart?"
      ],
      "metadata": {
        "id": "r2jJGEOYphqO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Above data shows us that out of customer with international plan 42.4% customer churn.This can due to high charges or connectivity issues, since cutomers already pay more tariff for interational calls compared to normal domestic call,if they have connectivity issues customers are bound to be unsatisfied, which leads to churn."
      ],
      "metadata": {
        "id": "Po6ZPi4hphqO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 3. Will the gained insights help creating a positive business impact? \n",
        "Are there any insights that lead to negative growth? Justify with specific reason."
      ],
      "metadata": {
        "id": "b0JNsNcRphqO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "the insights found will definitely help for a positive business impact. Those people who have international plan they are paying some additional charges to get the plan but the talk time value charge is same as those customers having no international plan. That might be great reason for more churns for those having international plan."
      ],
      "metadata": {
        "id": "xvSq8iUTphqO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Chart - 8"
      ],
      "metadata": {
        "id": "BZR9WyysphqO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#curn rate for customer with and without voice mail paln\n",
        "Voice_mail = pd.crosstab(churn_df[\"Voice mail plan\"],churn_df[\"Churn\"])\n",
        "Voice_mail['Churn_%'] = Voice_mail.apply(lambda x : x[1]*100/(x[0]+x[1]),axis = 1)\n",
        "print(Voice_mail)"
      ],
      "metadata": {
        "id": "TdPTWpAVphqO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "'''Detailed plot of churned and non churned customer vs. customer with voice \n",
        "mail plan ''' \n",
        "sns.countplot(x='Voice mail plan',hue=\"Churn\",data = churn_df)"
      ],
      "metadata": {
        "id": "7PLdmPl8pFQQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 1. Why did you pick the specific chart?"
      ],
      "metadata": {
        "id": "jj7wYXLtphqO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Countplot method is used to Show the counts of observations in each categorical bin using bars."
      ],
      "metadata": {
        "id": "Ob8u6rCTphqO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 2. What is/are the insight(s) found from the chart?"
      ],
      "metadata": {
        "id": "eZrbJ2SmphqO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Here, as we can see their is no clear relation that we can find between the customers with voice maill plan vs. people who churned "
      ],
      "metadata": {
        "id": "mZtgC_hjphqO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 3. Will the gained insights help creating a positive business impact? \n",
        "Are there any insights that lead to negative growth? Justify with specific reason."
      ],
      "metadata": {
        "id": "rFu4xreNphqO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Yes, voice mail plan might be considered partially."
      ],
      "metadata": {
        "id": "ey_0qi68phqO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Chart - 9"
      ],
      "metadata": {
        "id": "YJ55k-q6phqO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Customer Service Calls \n",
        "pd.crosstab(churn_df['Churn'], churn_df[\"Customer service calls\"], margins=True)"
      ],
      "metadata": {
        "id": "B2aS4O1ophqO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#churn rate with respect to no .of customer service calls.\n",
        "Customer_service = pd.crosstab(churn_df['Customer service calls'],churn_df[\"Churn\"])\n",
        "Customer_service['Churn_%'] = Customer_service.apply(lambda x : x[1]*100/(x[0]+x[1]),axis = 1)\n",
        "print(Customer_service)"
      ],
      "metadata": {
        "id": "TV9yoxyyrjFP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Histogram of Customer Serice calls grouped by churn  \n",
        "plt.rcParams['figure.figsize'] = (8, 6)\n",
        "sns.countplot(x=\"Customer service calls\", hue='Churn', data=churn_df);"
      ],
      "metadata": {
        "id": "gDuuK6warpxG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 1. Why did you pick the specific chart?"
      ],
      "metadata": {
        "id": "gCFgpxoyphqP"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Countplot method is used to Show the counts of observations in each categorical bin using bars."
      ],
      "metadata": {
        "id": "TVxDimi2phqP"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 2. What is/are the insight(s) found from the chart?"
      ],
      "metadata": {
        "id": "OVtJsKN_phqQ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "It can be stated that the churn rate increases from 4 calls to the service center. Customers who have called customer service three or fewer times have a markedly lower churn rate than that of customers who have called customer service four or more times."
      ],
      "metadata": {
        "id": "ngGi97qjphqQ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 3. Will the gained insights help creating a positive business impact? \n",
        "Are there any insights that lead to negative growth? Justify with specific reason."
      ],
      "metadata": {
        "id": "lssrdh5qphqQ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Customer service is an essential factor for every business. So definitely good customer service will have a positive impact to the business. We have to look after the customer calls and customer query report resolution duration. Need to optimize the time period. If one type of issue is coming from more than 5 customers, root cause analysis should be done on that same issue and should be resolved for everyone. Need to reduce the calls for each customer and he should be satisfied in a single call only. The customer service agents should be given great offer or recognition over great performance of customer issue resolution."
      ],
      "metadata": {
        "id": "tBpY5ekJphqQ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Chart - 14 - Correlation Heatmap"
      ],
      "metadata": {
        "id": "NC_X3p0fY2L0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# find correlation between all colummns and rows of given dataframe.\n",
        "# Correlation Plot \n",
        "corr= churn_df.corr()\n",
        "corr.style.background_gradient().set_precision(1)"
      ],
      "metadata": {
        "id": "xyC9zolEZNRQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# above data can also the diplayed in more detailed and colourful way by below code\n",
        "plt.figure(figsize=(20,10))\n",
        "churn_heatmap=churn_df.corr()\n",
        "sns.heatmap(abs(churn_heatmap),annot=True)"
      ],
      "metadata": {
        "id": "fZEeT8qbyVdL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 1. Why did you pick the specific chart?"
      ],
      "metadata": {
        "id": "UV0SzAkaZNRQ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "The correlation coefficient is a measure of the strength and direction of a linear relationship between two variables. A correlation matrix is used to summarize the relationships among a set of variables and is an important tool for data exploration and for selecting which variables to include in a model. The range of correlation is [-1,1]."
      ],
      "metadata": {
        "id": "DVPuT8LYZNRQ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 2. What is/are the insight(s) found from the chart?"
      ],
      "metadata": {
        "id": "YPEH6qLeZNRQ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "From the above correlation heatmap, we can see total day charge & total day minute, total evening charge & total evening minute, total night charge & total night minute are positiveliy highly correlated with a value of 1.\n",
        "\n",
        "Customer service call is positively correlated only with area code and negative correlated with rest variables."
      ],
      "metadata": {
        "id": "bfSqtnDqZNRR"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### Chart - 15 - Pair Plot "
      ],
      "metadata": {
        "id": "q29F0dvdveiT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Pair Plot\n",
        "sns.pairplot(churn_df, hue=\"Churn\")\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "o58-TEIhveiU"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 1. Why did you pick the specific chart?"
      ],
      "metadata": {
        "id": "EXh0U9oCveiU"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "A pairplot, also known as a scatterplot matrix, is a visualization that allows you to visualize the relationships between all pairs of variables in a dataset. It is a useful tool for data exploration because it allows you to quickly see how all of the variables in a dataset are related to one another."
      ],
      "metadata": {
        "id": "eMmPjTByveiU"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##### 2. What is/are the insight(s) found from the chart?"
      ],
      "metadata": {
        "id": "22aHeOlLveiV"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "From the above chart we got to know, there are less linear relationship between variables and data points aren't linearly separable. Churned customers data is clustered and ovearlapped each other. Non churn data are quite symmetrical in nature and churned customer data are quite non symmetric in nature. In this whole pair plot, the importance of area code can be seen and the number of churn with respect to different features are really insightful. Rest insights can be depicted from the above graph."
      ],
      "metadata": {
        "id": "uPQ8RGwHveiV"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **5. Solution to Business Objective**"
      ],
      "metadata": {
        "id": "JcMwzZxoAimU"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### What do you suggest the client to achieve Business Objective ? \n",
        "Explain Briefly."
      ],
      "metadata": {
        "id": "8G2x9gOozGDZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "* They should improve in covrage area and solving network issues (both domestic as well as international.\n",
        "* Give discount or create a plan in which as the day call mins increases above certain level the charges(i.e. the tariff per min) decrease means they are charged lower as compared to normal per min tariff.\n",
        "* lower the interational plan tariff or provide with some discounts.\n",
        "*They can provide better customer service and provide better problem solution, also take their feedback and work on the feedback suggested by the customers\n",
        "*\tModify International Plan as the charge is same as normal one.\n",
        "*\tBe proactive with communication.\n",
        "*\tAsk for feedback often.\n",
        "*\tPeriodically throw Offers to retain customers.\n",
        "*\tLook at the customers facing problem in  the most churning states.\n",
        "*\tLean into  best customers. \n",
        "*\tRegular Server Maintenance.\n",
        "*\tSolving Poor Network Connectivity Issue.\n",
        "*\tDefine a roadmap for new customers.\n",
        "*\tAnalyze churn when it happens.\n",
        "*\tStay competitive."
      ],
      "metadata": {
        "id": "pASKb0qOza21"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Conclusion**"
      ],
      "metadata": {
        "id": "gCX9965dhzqZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "From the above exploratory data analysis this are the following conclusions that can be incurred:\n",
        "* Some states have higher churn rate than other, for which network issues could the reason because if the competitor company had low tariff for calls then most of the states would have shown the appprox same churn rate.\n",
        "* Area and Account lenght has no relation with churn rate, hence this columns can be omitted or it can be said that the data is redundant.\n",
        "* Customers with international plan ON has higher churn rate compared to customerswith international plan OFF , this could be because the customer could be unhappy with th high tariff cost or network issues.\n",
        "* It could been seen that customers with vmails more than 20 (approx.) has higher churn rate.\n",
        "* Customers with higher day call mins has higher churn rate compared to other , could be because of the higher charges which is quite obvious, frequent caller might have found some other company offering low tariff .\n",
        "*With other varaibles such as evening ,night calls no relation could be found.\n",
        "* The churn rate increases as the call to the service center increases. Customers who have called customer service three or fewer times have a markedly lower churn rate than that of customers who have called customer service four or more times."
      ],
      "metadata": {
        "id": "Fjb1IsQkh3yE"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### ***Hurrah! You have successfully completed your EDA Capstone Project !!!***"
      ],
      "metadata": {
        "id": "gIfDvo9L0UH2"
      }
    }
  ]
}