NUMBERS = 1 2 3 4 5 6 7 8 9 10
run:
		@echo "Query --------------------------> 1"
		($(foreach var,$(NUMBERS),(python3 ./query1/mapper1.py ./event$(var).txt |sort |python3 ./combiner.py);)) |sort -g|python3 ./query1/reducer1.py >./query1/result_event.txt
		
		@echo "Query --------------------------> 2"
		($(foreach var,$(NUMBERS),(python3 ./query2/mapper2.py ./event$(var).txt |sort |python3 ./combiner.py);)) |sort -g|python3 ./query2/reducer2.py >./query2/result_strong.txt

		@echo "Query --------------------------> 3"
		python3 ./query3/mapper3.py ./query2/result_strong.txt |sort -g|python3 ./query3/reducer3.py >./query3/result_common.txt


		@echo "Query --------------------------> 4"
		python3 ./query4/mapper4.py|sort|python3 ./query4/reducer4.py > ./query4/result_shortest.txt



