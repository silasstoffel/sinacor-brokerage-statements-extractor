clean-csv:
	@echo "Cleaning up CSV files..."
	rm -Rf ./outputs/*.csv

clean-pdf:
	@echo "Cleaning up PDF files..."
	rm -Rf ./inputs/*.pdf

clean-io: clean-csv clean-pdf
	@echo "All clean up done."