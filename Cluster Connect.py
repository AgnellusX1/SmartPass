from flask import Flask, render_template, request, jsonify
import pickle
from scipy.spatial import distance
from password_strength import PasswordStats

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('MLpg.html')


@app.route("/", methods=["POST"])
def clus():
    with open('model1.pkl', 'rb') as f:
        kmeans = pickle.load(f)
        distances = []

        password = request.form['password']
        pass_len = len(password)
        pass_complex = PasswordStats(password).strength()

        for i in range(kmeans.n_clusters):
            p1 = (kmeans.cluster_centers_[i])
            p2 = (pass_len, pass_complex)
            d = distance.euclidean(p1, p2)
            distances.append(d)

        # print(distances)
        clus_names = ['Highly Breachable', 'Partially Unbreachable', 'Partially Breachable', 'Highly UnBreachable']
        low = distances.index(min(distances))
        result = clus_names[low]
        return jsonify({"pw": result})


if __name__ == '__main__':
    app.run(debug=True)
