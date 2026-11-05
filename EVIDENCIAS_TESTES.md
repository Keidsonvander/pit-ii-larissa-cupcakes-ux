# Evidências dos Testes e Correções — PIT II

**Aluna:** Larissa Razori Barbosa  
**RGM:** 33708266  
**Projeto:** Aplicativo de cupcakes com foco em interface, navegação e experiência do usuário

## 1. Destaque do fluxo de navegação
**Problema identificado:** a indicação das etapas do fluxo não mostrava de forma suficientemente clara em qual momento da navegação o usuário se encontrava.

**Correção aplicada:** as etapas Início, Catálogo, Carrinho, Finalização e Confirmação passaram a possuir destaque visual dinâmico conforme a ação realizada.

**Evidência:** atualização do componente de etapas e inclusão da função `marcarEtapa()` no arquivo `index.html`.

## 2. Confirmação ao adicionar produto
**Problema identificado:** a mensagem após adicionar um cupcake ao carrinho apresentava pouco destaque.

**Correção aplicada:** foram criados estilos distintos para mensagens de sucesso e erro, com texto mais claro e maior contraste.

**Evidência:** classes `msg ok` e `msg erro` adicionadas ao código.

## 3. Validação dos campos obrigatórios
**Problema identificado:** a orientação era genérica quando dados do pedido não eram preenchidos.

**Correção aplicada:** o sistema passou a verificar nome, telefone e endereço e informar exatamente quais campos precisam ser completados.

**Evidência:** nova lógica de validação no evento de finalização do formulário.

## 4. Responsividade e espaçamento
**Problema identificado:** em telas menores, alguns elementos ficavam muito próximos.

**Correção aplicada:** foram ampliados os espaçamentos do formulário, áreas de toque, campos e marcadores do fluxo.

**Evidência:** novas regras adicionadas ao media query para telas de até 600 pixels.

## 5. Confirmação final
**Problema identificado:** a confirmação final apresentava poucas informações sobre o pedido.

**Correção aplicada:** foi incluído um resumo final com número do pedido, nome, telefone, endereço e status de confirmação.

**Evidência:** novo bloco `confirmacao` inserido no `index.html`.

## Resultado da verificação
Após as correções, foram novamente verificados o catálogo, o carrinho, as mensagens, os campos obrigatórios, a navegação entre etapas, a confirmação final e o comportamento em telas menores. O fluxo principal apresentou funcionamento satisfatório e maior clareza para o usuário.

## Funcionalidades previstas para evolução futura
- cadastro e login de usuários;
- pagamento online real;
- integração com serviço de entrega;
- histórico de pedidos;
- acompanhamento de status após a finalização;
- testes em uma variedade maior de dispositivos e navegadores.
