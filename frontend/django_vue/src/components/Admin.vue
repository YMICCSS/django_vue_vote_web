<template>
  <div class="container mt-4">
    <h1 class="text-center mb-4">投票項目列表</h1>
    <div class="row">
      <div class="col-md-8 offset-md-2">
        <table class="table table-bordered">
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
                <button @click="deleteItem(item.id)" class="btn btn-danger btn-sm">刪除</button>
              </td>
            </tr>
          </tbody>
        </table>
        <form @submit.prevent="addItem" class="mt-4">
          <div class="form-group">
            <label for="item-name">新增投票項目:</label>
            <div class="input-group">
              <input type="text" id="item-name" v-model="newItem" required class="form-control">
              <div class="input-group-append">
                <button type="submit" class="btn btn-primary">新增</button>
              </div>
            </div>
          </div>
        </form>
        <div class="d-flex justify-content-center">
          <router-link to="/vote" class="btn btn-info mt-4">前往投票</router-link>
        </div>

      </div>
    </div>
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