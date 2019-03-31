import billboard

if __name__=='__main__':
    chart = billboard.ChartData('hot-100')
    print(chart)
    while chart.previousDate:
        print("Writing data ....")
        with open('charts.csv','a') as f:
            f.write(chart.__str__())
    print("Done.")
    
