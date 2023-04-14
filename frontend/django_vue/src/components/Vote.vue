<template>
    <div>
      <h1>投票項目列表</h1>
      <table>
        <thead>
          <tr>
            <th>投票項目</th>
            <th>得票數</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in items" :key="item.id">
            <td>{{ item.name }}</td>
            <td>{{ item.votes }}</td>
            <td>
              <input type="checkbox" :value="item.id" v-model="selectedItems" />
            </td>
          </tr>
        </tbody>
      </table>
      <form @submit.prevent="voteItem">
        <label for="voter-name">投票人名字:</label>
        <input type="text" id="voter-name" v-model="voterName" required />
        <br />
        <button type="submit">投票</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        items: [],
        selectedItems: [],
        voterName: ""
      };
    },
    mounted() {
      // 從 Django 後端取得投票項目列表
      this.fetchItems();
    },
    methods: {
      async fetchItems() {
        try {
          const response = await fetch("http://localhost:8000/api/items/");
          const data = await response.json();
          this.items = data;
        } catch (error) {
          console.error(error);
        }
      },
      async voteItem() {
        if (this.selectedItems.length > 0 && this.voterName.trim() !== "") {
          try {
            const response = await fetch("http://localhost:8000/api/votes/", {
              method: "POST",
              headers: {
                "Content-Type": "application/json"
              },
              body: JSON.stringify({
                items: this.selectedItems,
                voter_name: this.voterName
              })
            });
            const data = await response.json();
            // 更新投票項目的得票數
            data.forEach(item => {
              const index = this.items.findIndex(i => i.id === item.id);
              if (index !== -1) {
                this.items[index].votes = item.votes;
              }
            });
            this.selectedItems = [];
            this.voterName = "";
          } catch (error) {
            console.error(error);
          }
        }
      }
    }
  };
  </script>
  