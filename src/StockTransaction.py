#Written for Professor Jennifer Cohen
#By Andrew Owen (aka yumaikas)
#from Chapter 2 problem 10

import math
#This program retells the tale of Joe's experience with the stock market

#A pair of arrays used to store the
#information of each transaction in Joe's stock story
numberOfShares = [1000, 1000]
pricePerShare = [32.87, 33.92]
commissions = [0.0, 0.0]

#The percentage that Joe's broker gets as a commision
commissionFactor = 0.02
#run the calculations for the buy process
buyTotal = pricePerShare[0] * numberOfShares[0]
commissions[0] = buyTotal * commissionFactor
#calculate the sales total
saleTotal = pricePerShare[1] * numberOfShares[1]
commissions[1] = saleTotal * commissionFactor
#get the sum of the broker's pay
brokerFeeTotal = math.fsum(commissions)

PROFIT = (saleTotal - buyTotal) - brokerFeeTotal
status = "gain" if PROFIT > 0 else "loss"

#The details of the sale, for all the world to see
print "Joe paid ${total} for all the stock and his broker got a fee of ${fee}"\
      .format(total=buyTotal, fee=commissions[0])
print "He sold the stock for a total of ${total} and his broker got a fee of ${fee}"\
      .format(total=saleTotal, fee=commissions[1])
print "His broker ended up with a total of ${fee} in commissions"\
      .format(fee=brokerFeeTotal)
print "Joe ended up with a {status} of ${profit}".format(status=status,\
                                                         profit=PROFIT)
