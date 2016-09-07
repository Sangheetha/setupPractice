from firebase import firebase
firebase = firebase.FirebaseApplication('https://testapp-1ff42.firebaseio.com/', None)
result = firebase.delete('/Users', 'mnaidu')
print result
