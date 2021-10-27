from castle.algorithms import RL
from castle.datasets import load_dataset
from castle.common import GraphDAG
from castle.metrics import MetricsDAG
from castle.datasets import DAG, IIDSimulation

true_dag, X = load_dataset(name='iid_test')

# weighted_random_dag = DAG.erdos_renyi(n_nodes=10, n_edges=12, weight_range=(0.5, 2.0), seed=300)
# dataset = IIDSimulation(W=weighted_random_dag, n=2000, method='linear', sem_type='gauss')
# true_dag, X = dataset.B, dataset.X

n = RL(lambda_flag_default=True, nb_epoch=1000)

n.learn(X, dag=true_dag)

GraphDAG(n.causal_matrix, true_dag)
met = MetricsDAG(n.causal_matrix, true_dag)
print(met.metrics)
