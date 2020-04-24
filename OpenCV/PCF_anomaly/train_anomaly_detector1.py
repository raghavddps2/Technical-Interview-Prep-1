# USAGE
# python train_anomaly_detector.py --dataset forest --model anomaly_detector.model

# import the necessary packages
from featureFolder.features import load_dataset
from sklearn.ensemble import IsolationForest
from sklearn.cluster import MiniBatchKMeans
import argparse
import pickle

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to dataset of images")
ap.add_argument("-m", "--model", required=True,
	help="path to output anomaly detection model")
args = vars(ap.parse_args())

# load and quantify our image dataset
print("[INFO] preparing dataset...")
data = load_dataset(args["dataset"], bins=(3, 3, 3))

# train the anomaly detection model
print("[INFO] fitting anomaly detection model...")
model = MiniBatchKMeans(n_clusters = 2)
model.fit(data)

# serialize the anomaly detection model to disk
f = open(args["model"], "wb")
f.write(pickle.dumps(model))
f.close()