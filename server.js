import app from './src/App.js'; 
const port = process.send.PORT || 3400;

app.listen(port, ()=>{
    console.log(`API disponível em: localhost:${port}`)
});