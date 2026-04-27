from __future__ import print_function
import logging
import grpc
import EmployeeService_pb2
import EmployeeService_pb2_grpc
import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = EmployeeService_pb2_grpc.EmployeeServiceStub(channel)

        print("--- Testando Endpoints Originais ---")
        response = stub.ListAllEmployees(EmployeeService_pb2.EmptyMessage())
        print('Funcionários atuais: ' + str(len(response.employee_data)))

        print("\n--- Testando Novos Endpoints ---")
        name_res = stub.GetEmployeeName(EmployeeService_pb2.EmployeeID(id=101))
        print('Nome do funcionário 101: ' + name_res.name)

        count_res = stub.CountEmployees(EmployeeService_pb2.EmptyMessage())
        print('Total de funcionários no DB: ' + str(count_res.count))

if __name__ == '__main__':
    logging.basicConfig()
    run()
