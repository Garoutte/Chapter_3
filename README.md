# Chapter_3
###Computer code required to prepare data for annotation by MG-RAST

Determine the median coverage of a contig: Required software to run code:
Bowtie2 (v2.0.0-beta6)
SAMTools (v1.2)
BEDTools (v2.24.0)
Python (v2.7.2)
numpy (v1.6.1)

bowtie2 -x sample_contigs_mapping -U sample_reads.fastq -S sample_mapping.sam -p 4

samtools view -b -S sample_mapping.sam -t sample _contigs.fa > sample _mapping.bam

samtools sort sample_mapping.bam sample_mapping.sorted

samtools index sample_mapping.sorted.bam

bamToBed -i sample_mapping.sorted.bam > sample_mapping.bed

python get_length.py sample_contigs.fa > sample_genome_len.txt

genomeCoverageBed -i sample_mapping.bed -d -g sample_genome_len.txt > sample_mapping.g-cov.bed

python get_coverage.py sample_JGI_mapping.g-cov.bed > sample_mapping.coverage.txt

python add_abund.py  sample_mapping.coverage.txt sample_contigs.fa > sample_contigs_abund.fa


###BLAST search against CAZy database: Software required to run the code:
BLAST+ (v2.2.30)

blastx -num_threads 24 -query  sample_contigs.fa –db CAZy_2014-05-06_filt.fa  -evalue 1e-5 -task blastx -outfmt 6 –out sample.blastx.txt


###Computer code required to create minimum functional core.

#Establishing the 2 out of 3 sample core:
Python core_2_out_of_3.py sample1.txt sample2.txt sample3.txt > sample_core.txt

#Establishing the 2 out of 2 sample core:
Python compare_2.py sample_core1.txt sample_core2.txt > sample_core_combined.txt

