#  **GitLab CLI Scripts**

Some scripts that i've made to use in daily routines.

### **Pre-Req**

1. What it use:

    ```bash
    GitLab Personal Token and URL

    Python 3.7

    # Python Modules
    Python-GitLab 1.8.0
    Gitlab 1.0.2
    ```

2. More information for the modules  
    2.1 [Python-GitLab](https://python-gitlab.readthedocs.io/en/stable/index.html)   
    2.2 [GitLab API](https://docs.gitlab.com/ce/api/README.html)


## **Deploy**
1. Clone the project

2. Checkout to latest tag.

2. Install the requirements
    ```bash
    pip install -r requirements.txt
    ```

### **Configuration**

**There's only one config file:** <br>  

1. Copy the template config file:

    ```bash
    cp config/.python-gitlab.cfg.template config/.python-gitlab.cfg
    ```
    **Note:** The file .python-gitlab.cfg is marked as ignored by default,  doesn't seems a good idea to commit a credential file with production environment data.

2. Change the following fields:

    ```python
    url = http://gitlab.example.com
    private_token = froMO8upi6UspuStoCr7
    ```

3. You can create as many config groups as you want, just need to change which one you are calling the authentication in each script.