
import array_converter as ac
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Converts images to 64 x 64 grayscale images
#ic.image_converter()

# Converts each grayscale image into 1-D
# numpy arrays of length 4096
X,Y = ac.array_converter(270,360)

# # Preparing data frames
df = pd.DataFrame(X)
df['target'] = Y

labels = df['target']
data = df.drop(columns=['target'])

# # Creating training and test sets
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.40, random_state=10)

## Applying PCA to training set and selecting a number of components
## that explains at least 95% of variance
pca = PCA(n_components=0.95, svd_solver='full', whiten=True).fit(x_train)

# Projecting training data onto principal components
x_train_proj = pca.transform(x_train)

## Training classifier
clf = SVC(kernel='rbf', C=1000, gamma=0.01)
clf.fit(x_train_proj,y_train)

## Testing classifier

# Projecting test data onto principal components
x_test_proj = pca.transform(x_test)
Y_pred = clf.predict(x_test_proj)
print(classification_report(y_test,Y_pred))