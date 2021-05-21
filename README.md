<h1 align="center">X-Ray Anomaly Detection Models</h1>

This repository presents an ensemble based transfer learning approach for accurately classifying common thoracic diseases from Chest X-Rays (CXRs)

## Dataset
We use the [CheXpert](https://stanfordmlgroup.github.io/competitions/chexpert/) dataset for training and evaluation

## Models
The [final ensemble](Ensemble) consists of the following models
- [DenseNet-121](DenseNet-121)
- [DenseNet-169](DenseNet-169)
- [DenseNet-201](DenseNet-201)
- [Inception ResNet v2](Inception-ResNet-v2)
- [Xception](Xception)

The ensemble weights are found empirically while the disease-wise optimal prediction thresholds are found by maximizing the [Younden's J Statistic](https://en.wikipedia.org/wiki/Youden%27s_J_statistic)

## Results
The ROC curves for each individual model and the final ensemble are located [here](ROC-Curves)  
We achieve a mean area under the curve (AUC) of **0.915** on the validation set, that comes close to the SOTA of **0.94** (at the time of writing these models, i.e., May 2020)

## Illustration of a Model Pipeline Used

<p align="middle">
  <img src="img/XceptionPipeline.jpg" width="60%"></img>
</p>

## Illustration of the Final Ensemble

<p align="middle">
  <img src="img/Ensemble.jpg" width="60%"></img>
</p>

## Authors
[Harshit Varma](https://github.com/hrshtv), [Richeek Das](https://github.com/sudoRicheek), [Ankit Kumar Misra](https://github.com/ankitkmisra), [Prapti Kumar](https://github.com/praptikumar)
