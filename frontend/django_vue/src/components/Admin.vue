<template>
  <div>
    <h1>投票項目列表</h1>
    <table>
      <thead>
        <tr>
          <th>投票項目</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in items" :key="item.id">
          <td>{{ item.name }}</td>
          <td>
            <button @click="deleteItem(item.id)">刪除</button>
          </td>
        </tr>
      </tbody>
    </table>
    <form @submit.prevent="addItem">
      <label for="item-name">新增投票項目:</label>
      <input type="text" id="item-name" v-model="newItem" required />
      <button type="submit">新增</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
      newItem: ""
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
    async addItem() {
      if (this.newItem.trim() !== "") {
        try {
          const response = await fetch("http://localhost:8000/api/items/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify({ name: this.newItem })
          });
          const data = await response.json();
          this.items.push(data);
          this.newItem = "";
        } catch (error) {
          console.error(error);
        }
      }
    },
    async deleteItem(itemId) {
      try {
        await fetch(`http://localhost:8000/api/items/${itemId}/`, {
          method: "DELETE"
        });
        this.items = this.items.filter(item => item.id !== itemId);
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>
