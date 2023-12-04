# mock-operator

A mock k8s operator that creates text files in a hardcoded directory using a CRD.

To add the CRD to Kubernetes:

```bash
kubectl apply -f crd.yaml
```

To run the operator:

```bash
pip install kopf[uvloop]
kopf filemanagers.py --verbose
```

To create a `FileManager` deployment:

```bash
kubectl apply -f deployment.yaml
```

Then, you can see the files have been created:

```bash
ls /home/gntouts/kopferator/default
```

Now you can change the amount of files and reapply the deployment, delete the deployment, etc.