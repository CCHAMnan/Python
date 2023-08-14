# When d is too small

import owiener

c = 32431139421408969724831958231139785801888337292250206794518760840222560287550515647246258019193639765411883256840464493377997460419133290868788049010860967200701620427088947828092169968794877726781325415475267626701634986668199785769784906130394115183561459833404193151209793127468575365915732221188400029869
e = 21109574912625481065675031681698284627546341674151614175332807555399150602010182765042766452085530664759046322396431664649875691653623845013042114625647714031541019042563775685616909165324516805355669797666921069428524519883622108019673801781702819134381039042782048100529812336697232976329888475052360567991
n = 127865735232112386894848577601922577534490128710043599850842544209397608001865197699334768514163686239177964851214973455890644117051273589815640025240971320684063263593538690327809650027669877353277194687548072615328969561611367716704986688438218913476217966761475092934375525186368277166649403311247119003017
d = owiener.attack(e, n)

if d is None:
    print("Failed")
else:
    print("Hacked d={}".format(d))
    
    M = pow(c, d, n)
    print("Decrypted message: ", M)