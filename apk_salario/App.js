import { StyleSheet, Text, View, TextInput, TouchableOpacity } from 'react-native';
import { useState } from 'react'

export default function App() {
  const [valor, setValor] = useState("")

  function Imprimir(){
    return console.log(valor)
  }

  return (
    <View style={styles.container}>
      <Text style={styles.texto}> Salario: </Text>
    
      <TextInput value={valor} onChangeText={setValor} placeholder='Digite o valor!'/>
      
      <TouchableOpacity style={styles.button} onPress={Imprimir}>
        <Text>Calcular</Text>
      </TouchableOpacity>

    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  texto: {
    
  }
});
