from pycm import *

y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]

cm = ConfusionMatrix(actual_vector=y_actu, predict_vector=y_pred)

print(cm.classes)
print(cm.table)
print(cm)
