import graphs
import scc
import matplotlib.pyplot as mp
from numpy import mean
from timeit import default_timer as timer


def graph_creation_and_scc_times(num_of_nodes):
    num_of_arcs = 0
    max_num_of_arcs = num_of_nodes ** 2

    creation_times = []
    scc_times = []

    while num_of_arcs <= max_num_of_arcs:
        time = timer()
        # Create graph
        graph = graphs.Graph(num_of_nodes, num_of_arcs)
        time = timer() - time
        creation_times.append(time)

        time = timer()
        # Find strongly connected components
        scc.strongly_connected_components(graph)
        time = timer() - time
        scc_times.append(time)

        num_of_arcs += 1
    return creation_times, scc_times


def test(num_of_nodes):
    x_axis = []
    creation_times, scc_times = graph_creation_and_scc_times(num_of_nodes)

    creation_total_time = 0
    for i in creation_times:
        creation_total_time += i
    print 'Creation total time (', num_of_nodes, 'nodes):', creation_total_time

    scc_total_time = 0
    for i in scc_times:
        scc_total_time += i
    print 'SCC total time (', num_of_nodes, 'nodes):', scc_total_time

    for i in xrange(len(creation_times)):
        x_axis.append(i)

    mp.plot(x_axis, creation_times)
    mp.xlabel('Number of arcs')
    mp.title('Creation time with ' + str(num_of_nodes) + ' nodes')
    fig = mp.gcf()
    fig.canvas.set_window_title('Creation time with ' + str(num_of_nodes) + ' nodes')
    mp.show()

    mp.plot(x_axis, scc_times)
    mp.xlabel('Number of arcs')
    mp.title('SCC search time with ' + str(num_of_nodes) + ' nodes')
    fig = mp.gcf()
    fig.canvas.set_window_title('SCC search time with ' + str(num_of_nodes) + ' nodes')
    mp.show()

    return scc_times


def main():
    nodes = (2, 4, 8, 16, 32, 64)

    # recupero i tempi di SCC come risultato dei test
    times = []
    for node in nodes:
        times.append(test(node))

    # raccolgo in una lista il valore medio di ogni misurazione
    times_to_plot = []
    for i in times:
        times_to_plot.append(mean(i))

    # genero l'asse X
    x_axis = []
    number_of_tests = len(nodes)

    for i in xrange(number_of_tests):
        x_axis.append(i)

    # stampo i valori
    mp.plot(x_axis, times_to_plot)
    mp.title('Aggregato tempi di esecuzione algoritmo SCC')
    mp.show()


if __name__ == '__main__':
    main()
