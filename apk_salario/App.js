import { StyleSheet, Text, View, TextInput, TouchableOpacity } from 'react-native';
import { useState } from 'react'

export default function App() {
  const [valor, setValor] = useState("");
  const [resultado, setResultado] = useState("");

  function Imprimir(){
    return setResultado("lol");
  }

  function Limpar() {
    return setResultado("")
  }

  return (
    <View style={styles.container}>
      <Text style={styles.texto}> Salario: </Text>
    
      <TextInput value={valor} onChangeText={setValor} placeholder='Digite o valor!'/>
      
      <TouchableOpacity style={styles.button} onPress={Imprimir}>
        <Text>Calcular</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button} onPress={Limpar}>
        <Text>Limpar</Text>
      </TouchableOpacity>

      <View>
        <Text>Resultado: </Text>
        <Text> {resultado}</Text>
      </View>

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
