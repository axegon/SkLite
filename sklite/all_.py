"""Importing all the implemented models and storing
them in a dict."""
from .lib.models.tree import SkliteDecisionTreeClassifier
from .lib.models.naive_bayes import SkliteBernoulliNBClasifier, \
    SkliteGaussianNBClassifier
from .lib.models.neighbors import SkliteKNeighborsClassifier
from .lib.models.svc import SkliteLinearSVCClassifier, SkliteSVCClassifier
from .lib.models.neural_network import SkliteMLPClassifierClassifier
from .lib.models.ensemble import SkliteRandomForestClassifier

AVAILABLE_ = {
    "RandomForestClassifier": SkliteRandomForestClassifier,
    "MLPClassifier": SkliteMLPClassifierClassifier,
    "LinearSVC": SkliteLinearSVCClassifier,
    "SVC": SkliteSVCClassifier,
    "KNeighborsClassifier": SkliteKNeighborsClassifier,
    "BernoulliNB": SkliteBernoulliNBClasifier,
    "GaussianNB": SkliteGaussianNBClassifier,
    "DecisionTreeClassifier": SkliteDecisionTreeClassifier
}
