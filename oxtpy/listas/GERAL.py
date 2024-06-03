list=[]

x=1
aux=[]

list.append(x)

# equivalente a lista[len[lista]:]=[x]

# node* add(node *head, int item){
#     node *new_node=(node*) malloc(sizeof(struct node));
#     new_node->item=item;
#     new_node->next=NULL;

#     if(head==NULL) return new_node;

#     struct node *current=head;

#     while(current->next!=NULL){
#         current=current->next;    
#     }

#     current->next=new_node;

#     return head;
# }


list.extend(aux)

# faz vários list.append(x) de uma vez, adicionando vários elementos ao fim de outra lista
# equivalente a lista[len(lista):]=[1,2,3]

# node* extend(node *head, int items[], int size) {
#     for (int i = 0; i < size; i++) {
#         head = add(head, items[i]);
#     }
#     return head;
# }


list.insert(0,x)

#list.insert(len(list), x) e equivale a list.append(x).
#insere um número x na posição 0 da lista

# node* insert(node* head, int index, int item) {
#     node* new_node = (node*)malloc(sizeof(node));
#     new_node->item = item;

#     if (index == 0) {
#         new_node->next = head;
#         return new_node;
#     }

#     node* current = head;
#     for (int i = 0; current != NULL && i < index - 1; i++) {
#         current = current->next;
#     }

#     if (current == NULL) {
#         free(new_node);
#         return head;
#     }

#     new_node->next = current->next;
#     current->next = new_node;

#     return head;
# }


list.pop([x])

# retira o elemento da posição x
# se não houver nenhum parametro, ira tirar e retornar o ultimo elemento da lista

# int pop(node** head_ref, int index) {
#     if (*head_ref == NULL) return -1;

#     node* temp = *head_ref;

#     if (index == 0) {
#         *head_ref = temp->next;
#         int item = temp->item;
#         free(temp);
#         return item;
#     }

#     for (int i = 0; temp != NULL && i < index - 1; i++) {
#         temp = temp->next;
#     }

#     if (temp == NULL || temp->next == NULL) return -1;

#     node* next = temp->next->next;
#     int item = temp->next->item;
#     free(temp->next);
#     temp->next = next;

#     return item;
# }


list.index(x)

# retorna a posição do primeiro numero encontrado igual a x

# int index(node* head, int item) {
#     int index = 0;
#     node* current = head;

#     while (current != NULL) {
#         if (current->item == item) {
#             return index;
#         }
#         current = current->next;
#         index++;
#     }

#     return -1;  // Retorna -1 se o item não for encontrado
# }


list.reverse(aux)

# inverte a ordem dos elementos na lista

# node* reverse(node* head) {
#     node* prev = NULL;
#     node* current = head;
#     node* next = NULL;

#     while (current != NULL) {
#         next = current->next;
#         current->next = prev;
#         prev = current;
#         current = next;
#     }

#     return prev;
# }


list.sort()

# lista.sort() ordena normalmente
# lista.sort(reverse=True) ordena em ordem decrescente
# lista.sort(key=len) ordena crescente conforme o tamanho da string
# mergeSort


list.remove(x)
# remove o primeiro numeor x encontrado na lista
#ValueError caso x nao esteja contido


list.clear()
# remove todos os itens de uma lista
# equivalente a del a[:]


list.copy()
# devolve uma cópia rasa da lista
# equivalente a a[:]

list.count()
# devolve o número de vezes em que x aparece na lista


############################################


# TUPLAS:
# -estruturas imutaveis 
# -criadas com ()
# -elementos acessados com []
# -suporte a descompactação
# -varios metodos iguais às listas


# MATRIZES:
# -listas de listas
# -elementos acessados por [][]
# -iteração por linhas e elementos
# -metodos removem e adicionam linhas