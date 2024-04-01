import { StyleSheet, Text, View, TextInput, TouchableOpacity } from 'react-native';
import { useState } from 'react'

export default function App() {
  const [valor, setValor] = useState("");
  const [resultado, setResultado] = useState("");

  function Imprimir(){
    return setResultado(`Você digitou ${valor}`);
  }

  function Limpar() {
    return setResultado("") & setValor("")
  }

  return (
    <View style={styles.container}>
      <Text style={styles.texto}> Salario: </Text>
    
      <TextInput value={valor} onChangeText={setValor} placeholder='Digite o valor!'/>
      <View style={styles.salario}>
        <TouchableOpacity style={styles.button} onPress={Imprimir} >
          <Text style={styles.texto}>Calcular</Text>
        </TouchableOpacity>

        <TouchableOpacity style={styles.button} onPress={Limpar}>
          <Text style={styles.box_direita}>Limpar</Text>
        </TouchableOpacity>
      </View>

      <View>
        <Text style={styles.texto}>Resultado: </Text>
        <Text > {resultado}</Text>
      </View>

    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  salario: {
    flexDirection: 'row',
  },
  button: {
    margin: 5,
    padding: 10,
    backgroundColor: 'lightblue',
    borderRadius: 5,
  },
  texto: {
    color: 'white',
    fontWeight: 'bold',
  },
  box_direita: {
    color: 'white',
    fontWeight: 'bold',
    
  },
});
