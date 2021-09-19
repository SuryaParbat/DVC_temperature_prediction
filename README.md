Create environment

```terminal
conda create -n DVC python=3.9 -y
```

Activate Environment

```terminal
conda activate DVC
```

Create Req file

```terminal
type nul > requirements.txt
```

Install the req

```terminal
pip install -r requirements.txt
```

```terminal
git init
```

```terminal
dvc init 
```
```
git add . 
```
```
git commit -m "msg"
```
```buildoutcfg
git remote add origin https://
```

```buildoutcfg
git branch -M main
```

```buildoutcfg
git push origin main
```
create artifact filder
````buildoutcfg
mkdir artifacts
````

````buildoutcfg
mlflow server command - 
 mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 127.0.0.1 -p 5000

````

````buildoutcfg
pytest -v
````