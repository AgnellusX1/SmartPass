from flask import Flask, render_template, request, jsonify
import pickle
import matplotlib.pyplot as plt

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
        from password_strength import PasswordStats

        pass_complex = PasswordStats(password).strength()

        from scipy.spatial import distance

        for i in range(kmeans.n_clusters):
            p1 = (kmeans.cluster_centers_[i])
            # print(p1)
            p2 = (pass_len, pass_complex)
            d = distance.euclidean(p1, p2)
            distances.append(d)

        # print(distances)
        clus_names = ['Highly Breachable', 'Partially Unbreachable', 'Partially Breachable', 'Highly UnBreachable']
        low = distances.index(min(distances))
        target_cluster = kmeans.cluster_centers_[low]
        result = clus_names[low]
        return jsonify({"pw": result})
        # print(target_cluster)
        # print(low)
        # print("Your Password Belong to the Category of")
        # print(clus_names[low])
        # return render_template('MLpg.html', password_res=clus_names[low])
        # return clus_names[low]

        # Visualising the clusters
        # plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s=100, c='red', label='Very Weak')
        # plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s=100, c='orange', label='Good')
        # plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s=100, c='blue', label='Week')
        # plt.scatter(x[y_kmeans == 3, 0], x[y_kmeans == 3, 1], s=100, c='green', label='Great')
        # plt.scatter(pass_len, pass_complex, c='pink', label='Your Password', s=300)
        # plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='black', label='Centroids')
        # plt.ylabel('Complexity')
        # plt.xlabel('Length of Passwords')
        # plt.legend()
        # plt.show()


# @app.route('/',methods=[POST])
# def getvalue():
#     if request.method == 'POST':

#         name = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         return render_template('MLpg.html', u=name , e = email , p = password)

if __name__ == '__main__':
    app.run(debug=True)
