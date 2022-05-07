# TO DO
import biology

def test_est_base():
    assert biology.est_base("R")==False
    assert biology.est_base("T")==True
    assert biology.est_base("C")==True
    assert biology.est_base("Z")==False
    print("Test de la fonction : OK ")

test_est_base()

def test_est_adn():
    assert biology.est_adn("ATCCCGGGGTAFATGG")==False
    assert biology.est_adn("ATGGGTAACAA")==True
    assert biology.est_adn("ZETUVJD")==False
    assert biology.est_adn("0004832")==False
    print("Test de la fonction : OK ")

test_est_adn()

def test_arn():
    assert biology.arn("AZTGGCCC")== None
    assert biology.arn("ATGGTCC")=="AUGGUCC"
    assert biology.arn("AGGCC")=="AGGCC"
    assert biology.arn("TTTTTT")=="UUUUUU"
    print("Test de la fonction : OK ")

test_arn()

def test_arn_to_codons():
    assert biology.arn_to_codons("CGAGUG")==['CGA', 'GUG']
    assert biology.arn_to_codons("CUCGUG")==['CUC', 'GUG']
    assert biology.arn_to_codons("CUCGUUUG")==['CUC', 'GUU']
    assert biology.arn_to_codons("CUCGG")==['CUC']
    print("Test de la fonction : OK ")

test_arn_to_codons()

def test_load_dico_codons_aa():
    assert biology.load_dico_codons_aa(r"D:\Projet\Initiation au dev 2\Partie_2\sae_s01.02-main\data/codons_aa.json")=={'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine', 'UUG': 'Leucine', 'CUU': 'Leucine', 'CUC': 'Leucine', 'CUA': 'Leucine', 'CUG': 'Leucine', 'AUU': 'Isoleucine', 'AUC': 'Isoleucine', 'AUA': 'Methionine', 'AUG': 'Methionine', 'GUU': 'Valine', 'GUC': 'Valine', 'GUA': 'Valine', 'GUG': 'Valine', 'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine', 'CCU': 'Proline', 'CCC': 'Proline', 'CCA': 'Proline', 'CCG': 'Proline', 'ACU': 'Threonine', 'ACC': 'Threonine', 'ACA': 'Threonine', 'ACG': 'Threonine', 'GCU': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine', 'GCG': 'Alanine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'CAU': 'Histidine', 'CAC': 'Histidine', 'CAA': 'Glutamine', 'CAG': 'Glutamine', 'AAU': 'Asparagine', 'AAC': 'Asparagine', 'AAA': 'Lysine', 'AAG': 'Lysine', 'GAU': 'Aspartic acid', 'GAC': 'Aspartic acid', 'GAA': 'Glutamic acid', 'GAG': 'Glutamic acid', 'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGA': 'Tryptophan', 'UGG': 'Tryptophan', 'CGU': 'Arginine', 'CGC': 'Arginine', 'CGA': 'Arginine', 'CGG': 'Arginine', 'AGU': 'Serine', 'AGC': 'Serine', 'GGU': 'Glycine', 'GGC': 'Glycine', 'GGA': 'Glycine', 'GGG': 'Glycine'}
    print("Test de la fonction : Ok")

test_load_dico_codons_aa()

def test_codons_stop():
    assert biology.codons_stop(biology.load_dico_codons_aa(r"D:\Projet\Initiation au dev 2\Partie_2\sae_s01.02-main\data/codons_aa.json"))==['AGA', 'AGG', 'UAA', 'UAG']
    print("Test de la fonction : OK")

test_codons_stop()

def test_codons_to_aa():
    assert biology.codons_to_aa(["CGU", "AAU", "UGA", "UAG", "CGU"],biology.load_dico_codons_aa(r"D:\Projet\Initiation au dev 2\Partie_2\sae_s01.02-main\data/codons_aa.json"))==['Arginine', 'Asparagine', 'Tryptophan']
    assert biology.codons_to_aa([ "UAA", "UGA", "UAC", "CGU"],biology.load_dico_codons_aa(r"D:\Projet\Initiation au dev 2\Partie_2\sae_s01.02-main\data/codons_aa.json"))==[]
    assert biology.codons_to_aa([ "GGA", "UGG", "UAAC", "CGU"],biology.load_dico_codons_aa(r"D:\Projet\Initiation au dev 2\Partie_2\sae_s01.02-main\data/codons_aa.json"))==['Glycine', 'Tryptophan']
    print("Test de la fonction : OK")

test_codons_to_aa()

def test_nextIndice():
    assert biology.nextIndice(["bonjour", "hello", "buongiorno", "ciao","bye"],1,["hello","bye"])==1
    assert biology.nextIndice(["bonjour", "hello", "buongiorno", "ciao","bye"],2,["hello","bye"])==4
    assert biology.nextIndice(["bonjour", "hello", "buongiorno", "ciao","bye"],3,["hello","bye"])==4
    assert biology.nextIndice(["bonjour", "hello", "buongiorno", "ciao","bye"],5,["hello","bye"])==4
    print("Test de la fonction : OK")
    
test_nextIndice()

def test_decoupe_sequence():
    assert biology.decoupe_sequence(["val1", "début", "val2", "val3", "end", "val4", "fin", "begin", "val5", "fin", "val6"],["début", "begin"],["fin", "end"])==[['val2', 'val3'], ['val5']]
    assert biology.decoupe_sequence(["val1", "début", "val2", "val3", "end","val49", "val4", "fin", "begin","val5", "fin", "val6"],["début", "begin"],["fin", "end"])==[['val2', 'val3'], ['val5']]
    assert biology.decoupe_sequence(["val1", "début", "val2", "end", "val3", "val4", "fin", "begin","val5", "fin", "val6"],["début", "begin"],["fin", "end"])==[['val2'], ['val5']]
    print("Test de la fonction : OK")
    
test_decoupe_sequence()

def test_codons_to_seq_codantes():
    assert biology.codons_to_seq_codantes(["CGU", "UUU", "AUG", "CGU", "AUG", "AAU", "UAA", "AUG", "GGG", "CCC",  "CGU", "UAG", "GGG"],biology.load_dico_codons_aa(r"D:\Projet\Initiation au dev 2\Partie_2\sae_s01.02-main\data/codons_aa.json"))==[['CGU', 'AUG', 'AAU'], ['GGG', 'CCC', 'CGU']]
    assert biology.codons_to_seq_codantes(["CGU", "UUU", "AUG","UUU", "CGU", "AUG", "AAU", "UAA", "AUG", "GGG", "CCC",  "CGU", "UAG", "GGG"],biology.load_dico_codons_aa(r"D:\Projet\Initiation au dev 2\Partie_2\sae_s01.02-main\data/codons_aa.json"))==[['UUU', 'CGU', 'AUG', 'AAU'], ['GGG', 'CCC', 'CGU']]
    assert biology.codons_to_seq_codantes(["CGU", "UUU", "AUG","AAU", "CGU", "AUG", "AAU", "UAA", "AUG", "GGG", "CCC",  "CGU", "UAG","CGU", "GGG"],biology.load_dico_codons_aa(r"D:\Projet\Initiation au dev 2\Partie_2\sae_s01.02-main\data/codons_aa.json"))==[['AAU', 'CGU', 'AUG', 'AAU'], ['GGG', 'CCC', 'CGU']]
    print("Test de la fonction : OK")
    
test_codons_to_seq_codantes()


def test_seq_codantes_to_seq_aas():
    assert biology.seq_codantes_to_seq_aas([["CGU", "AUG", "AAU"],["GGG", "CCC", "CGU"]],biology.load_dico_codons_aa(r"D:\Projet\Initiation au dev 2\Partie_2\sae_s01.02-main\data/codons_aa.json"))==[['Arginine', 'Methionine', 'Asparagine'], ['Glycine', 'Proline', 'Arginine']]
    assert biology.seq_codantes_to_seq_aas([["CGU", "AUG", "CCC"],["UUU", "CCC", "CGU"]],biology.load_dico_codons_aa(r"D:\Projet\Initiation au dev 2\Partie_2\sae_s01.02-main\data/codons_aa.json"))==[['Arginine', 'Methionine', 'Proline'],['Phenylalanine', 'Proline', 'Arginine']]
    print("Test de la fonction : OK")

test_seq_codantes_to_seq_aas()


def test_adn_encode_molecule():
    assert biology.adn_encode_molecule("CGTTTTATGCGTATGAATTAAATGGGGCCCCGTTAGGGG",biology.load_dico_codons_aa(r"D:\Projet\Initiation au dev 2\Partie_2\sae_s01.02-main\data/codons_aa.json"),["Glycine", "Proline", "Arginine"])==True
    assert biology.adn_encode_molecule("CGGGGTTTTATGCGTATGAATTAAATGGGGCCCCGTTAGGGG",biology.load_dico_codons_aa(r"D:\Projet\Initiation au dev 2\Partie_2\sae_s01.02-main\data/codons_aa.json"),["Glycine", "Proline", "Arginine"])==True
    assert biology.adn_encode_molecule("CGGGGTTTTATGCGTATGAATTAAATGGGGCCCCGTTAGGGG",biology.load_dico_codons_aa(r"D:\Projet\Initiation au dev 2\Partie_2\sae_s01.02-main\data/codons_aa.json"),["Glycine", "Asparagine", "Arginine"])==False
    print("Test de la fonction : OK")
    
test_adn_encode_molecule()
