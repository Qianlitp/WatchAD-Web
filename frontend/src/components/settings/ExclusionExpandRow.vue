<template>
    <div>
        <Row v-for="rule in rules" class="expand-row">
            <Col span="8">
                <span class="expand-key">Field Name: </span>
                <span class="expand-value">{{ rule.field_name }}</span>
            </Col>
            <Col span="4">
                <span class="expand-key">Field Type: </span>
                <span class="expand-value">{{ rule.field_type }}</span>
            </Col>
            <Col span="4">
                <span class="expand-key">Match Type: </span>
                <span class="expand-value">{{ rule.match_type }}</span>
            </Col>
            <Col span="8">
                <span class="expand-key">Value: </span>
                <span class="expand-value">{{ rule.value }}</span>
            </Col>
        </Row>
    </div>
</template>

<script>
export default {
    name: "exclusion-expand-row",
    data() {
        return {

        }
    },
    props: {
        row: Object,
        required: true
    },
    computed: {
        rules() {
            return this.row["rules"]
        }
    }
};
</script>

<style scoped>
.expand-row {
    margin-top: 10px;
}

.expand-key {
    font-weight: 700
}
</style>