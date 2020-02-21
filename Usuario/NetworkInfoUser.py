def network_information_user_view(networkInformationList):
    for i in networkInformationList[0]:
        print("- " + str(i) + ":")
        for j in networkInformationList[0][str(i)]:
            print(str(j))
        print("Status:\n" + str(networkInformationList[1][i]))

        #Uso de dados de rede por interface
        print("Trânsito de Dados:\n" + str(networkInformationList[2][str(i)]))
        print()